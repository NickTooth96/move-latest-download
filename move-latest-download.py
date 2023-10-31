#!/usr/bin/env python3

import os
import sys
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate
import src.save_history as save_history


ERROR_msg =     f'\nMost recently downloaded file/files:\n\t{most_recent.find(download_path.find())}\nRetype command with "--one" to move <{most_recent.find(download_path.find())[0]}> or "--all" to move all listed files.\n'
dp = download_path.find()
mr = most_recent.find(dp)

if "range" in sys.argv:
    mr = most_recent.find(dp)
    print(sys.argv)
   

if "--find" in sys.argv:
  print(dp,mr)  
elif "--all" in sys.argv:
  relocate.move(mr,dp,os.getcwd())
elif "--one" in sys.argv:
  relocate.move(mr[0],dp,os.getcwd())
elif "--undo" in sys.argv:
  relocate.undo_last_move()
elif "--history" in sys.argv:
  save_history.read()
else:
  print(ERROR_msg)