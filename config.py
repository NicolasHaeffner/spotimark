import ui
import os
import pickle

dir_path = os.path.dirname(os.path.realpath(__file__))
conf_path = os.path.join(dir_path, 'cache', 'config')

def ok_tapped(sender):
    v.close()
    config={}
    config['client_id']=sender.superview['client_id'].text
    config['client_secret']=sender.superview['client_secret'].text
    config['username']=sender.superview['username'].text
    
    pickle.dump(config, open(conf_path, 'wb'))
    
    print(config)

if __name__ == '__main__':
    
    v = ui.load_view()
    
    if os.path.exists(conf_path):
        config = pickle.load(open(conf_path, 'rb'))
        v['client_id'].text = config['client_id']
        v['client_secret'].text = config['client_secret']
        v['username'].text = config['username']
    
    
    v.present('sheet')
