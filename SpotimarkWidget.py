#!python3

'''
This widget script shows a grid of shortcut buttons that launch URLs when tapped.

The shortcut titles/URLs and the grid layout can be configured with the SHORTCUTS, COLS, ROWS variables.
'''

import appex, ui
import os
from math import ceil, floor
from resources.helpers import genShortcuts

dir_path = os.path.dirname(os.path.realpath(__file__))
cachepath = os.path.join(dir_path, 'cache')
bookpath = os.path.join(cachepath, 'bookmarks')

# NOTE: The ROWS variable determines the number of rows in "compact" mode. In expanded mode, the widget shows all shortcuts.
COLS = 2
ROWS = 2

# Each shortcut should be a dict with at least a 'title' and 'url' key. 'color' and 'icon' are optional. If set, 'icon' should be the name of a built-in image.
SHORTCUTS = [
{'title': 'generate Bookmark', 'url': 'pythonista://spotimark-git/spotimark?Action=run&args=genBookmark', 'color': '#1ED760', 'icon': 'iow:plus_circled_24'},
{'title': 'delete Bookmark', 'url': 'pythonista://spotimark-git/spotimark?Action=run&args=delBookmark', 'color': '#ff0000', 'icon': 'iow:ios7_trash_outline_24'}
]
SHORTCUTS.extend(genShortcuts(bookpath))

class LauncherView (ui.View):
	def __init__(self, shortcuts, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for s in shortcuts:
			btn = ui.Button(title=' ' + s['title'], image=ui.Image(s.get('icon', 'iow:bookmark_24')), name=s['url'], action=self.button_action, bg_color=s.get('color', '#55bcff'), tint_color='#fff', corner_radius=9)
			self.add_subview(btn)
			self.buttons.append(btn)
	
	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw, i//COLS * bh, bw, bh).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		import webbrowser
		webbrowser.open(sender.name)

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	#if v is None or v.name != widget_name:
	v = LauncherView(SHORTCUTS)
	v.name = widget_name
	appex.set_widget_view(v)

if __name__ == '__main__':
	main()
	#print(SHORTCUTS)
