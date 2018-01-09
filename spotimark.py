#!/usr/local/bin/python3

import os
import sys
import webbrowser
import pickle
import dialogs
from resources.helpers import delShortcut


# config

dir_path = os.path.dirname(os.path.realpath(__file__))
cachepath = os.path.join(dir_path, 'cache')
bookpath = os.path.join(cachepath, 'bookmarks')
conf_path = os.path.join(dir_path, 'cache', 'config')
# username = 'Halbstark1708'
# client_id = '3368d46f576144bbbe5ddbdf4c8c090e'
# client_secret = '0046caed160942e5b4d1a8dd989c5958'
ip = 'localhost'
port = '9595'

if os.path.exists(conf_path):
    config = pickle.load(open(conf_path, 'rb'))
    client_id = config['client_id']
    client_secret = config['client_secret']
    username = config['username']
else:
    dialogs.alert('no config found, please run config.py')    



def spotimarkAction(action):

    if action == 'genBookmark':

        # get token
        import resources.spotipy.util as util
        import resources.spotipy.client as client
        token = util.prompt_for_user_token(username, cachepath, client_id=client_id, client_secret=client_secret, ip=ip, port=port)

        if token:
            sp = client.Spotify(auth=token)

            try:
                parsed = sp.current_user_playing_track()['item']
                message = 'Create/Update bookmark: ' + parsed['album']['name'] + ' - ' + parsed['name'] + '?'
                r = dialogs.alert('Bookmark created', message=message, button1='yes', button2='no', hide_cancel_button=True)
                if r == 1:
                    filepath = os.path.join(bookpath, parsed['album']['id'])
                    pickle.dump(parsed, open(filepath, 'wb'))
                    dialogs.hud_alert('okay - bookmark created')
                else:
                    dialogs.hud_alert('okay - cancelled')
            except:
                dialogs.alert('Error', message='nothing playing')
            

        else:
            print('Can\'t get token for ' + username)
            
    elif action == 'delBookmark':
        delShortcut(bookpath)
        
        
if __name__=='__main__':
    spotimarkAction(sys.argv[1])
 

