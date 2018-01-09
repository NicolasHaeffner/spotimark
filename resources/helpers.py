import pickle
import os
import dialogs



def genShortcuts(bookpath):
    bookmarks = []
    for filename in os.listdir(bookpath):
        book = pickle.load(open(os.path.join(bookpath, filename), 'rb'))
        entry = {'title': book['album']['name'], 'url': ('spotify://track/' + book['id'])}
        bookmarks.append(entry)

    return bookmarks

def delShortcut(bookpath):
    bookmarks = []
    for filename in os.listdir(bookpath):
        book = pickle.load(open(os.path.join(bookpath, filename), 'rb'))
        entry = {'title': book['album']['name'], 'filename': filename}
        bookmarks.append(entry)    
    
    ans = dialogs.list_dialog(title="chose bookmark to delete", items=bookmarks, multiple=False)
    if ans:
        os.remove(os.path.join(bookpath, ans['filename']))


if __name__ == '__main__':
    
    bookpath = '/private/var/mobile/Containers/Shared/AppGroup/C4F0858B-18EA-4EBD-A5D9-371A466F709C/Pythonista3/Documents/spotimark-git/cache/bookmarks'
    delShortcut(bookpath)
