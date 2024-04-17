#!/usr/bin/env python3

import os
import sys
import argparse
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate
import src.save_history as save_history

VERSION = "1.2.2"
NAME = "Move-Latest-Download"

ERROR_msg =     f'\nMost recently downloaded file/files:\n\t{most_recent.find(download_path.find())}\nRetype command with "--one" to move <{most_recent.find(download_path.find())[0]}> or "--all" to move all listed files.\n'
dp = download_path.find()
mr = most_recent.find(dp)

if "args" in sys.argv:
    print(sys.argv)

parser = argparse.ArgumentParser(description="Move most recently downloaded file/files to a specified directory.")
parser.add_argument("--find", help="Find most recently downloaded file/files.", action="store_true")
parser.add_argument("--all", help="Move all most recently downloaded file/files to specified directory.", action="store_true")
parser.add_argument("--one", help="Move only the most recently downloaded file to specified directory.", action="store_true")
parser.add_argument("--undo", help="Undo last move.", action="store_true")
parser.add_argument("--history", help="Show history of moved files.", action="store_true")
parser.add_argument("--redo", help="Redo previous move.", action="store_true")
parser.add_argument("--stat", help="Show statistics of moved files.", action="store_true")
parser.add_argument("--version", help="Show version of the program.", action="store_true")

args = parser.parse_args()

## Main

if args.find:
  print(dp,mr)
elif args.all:
  relocate.move(mr,dp,os.getcwd())
elif args.one:
  file = []
  file.append(mr[0])
  relocate.move(file,dp,os.getcwd())
elif args.undo:
  relocate.undo_last_move()
elif args.history:
  save_history.read()
elif args.redo:
  if sys.argv[sys.argv.index("--redo") + 1]:
    try:
      index = int(sys.argv[sys.argv.index("--redo") + 1])
    except:
      index = int(input("Enter number of items to list: "))
    relocate.redo_previous(index)
  else:
    relocate.redo_previous()
elif args.stat:
  save_history.stats()
elif args.version:
  print(NAME,VERSION)
else:
  print('Error: No arguments provided. Use "--help" for more information.')