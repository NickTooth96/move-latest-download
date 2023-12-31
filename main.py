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
VERSION = "1.1.1"

if "range" in sys.argv:
    mr = most_recent.find(dp)
    print(sys.argv)
   

if "--find" in sys.argv:
  print(dp,mr)  
elif "--all" in sys.argv:
  relocate.move(mr,dp,os.getcwd())
elif "--one" in sys.argv:
  file = []
  file.append(mr[0])
  relocate.move(file,dp,os.getcwd())
elif "--undo" in sys.argv:
  relocate.undo_last_move()
elif "--history" in sys.argv:
  save_history.read()
elif "--redo" in sys.argv:
  if sys.argv[sys.argv.index("--redo") + 1]:
    index = int(sys.argv[sys.argv.index("--redo") + 1])
    relocate.redo_previous(index)
  else:
    relocate.redo_previous()
else:
  print(ERROR_msg)