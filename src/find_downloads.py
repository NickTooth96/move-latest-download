import os 


def exists_downloads():
    user_path = os.path.expanduser('~')
    dir_list = os.listdir(user_path)

    for x in dir_list:
        if x in ['Downloads','downloads']: # try with regex - import re - re.match()
            print(x,os.path.exists(os.path.join(user_path,x))) # janky AF - only works if Downloads dir in user/[user]
            downloads_path = os.path.join(user_path,x)
    
    return downloads_path
exists_downloads()