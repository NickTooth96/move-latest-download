#!/usr/bin/env python3

import os
import sys
import argparse
import tomllib
import src.download_path as download_path
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate
import src.save_history as save_history


dp = download_path.find()
mr = most_recent.find(dp)

parser = argparse.ArgumentParser(
                    prog='mvld',
                    description='Finds the most recently downloaded file/files and moves them to a specified location.',
                    epilog='By Nicholas Toothaker')

parser.add_argument('-f','--find', action='store_true', help='Find the most recently downloaded file/files')
parser.add_argument('-a','--all', action='store_true', help='Move all listed files')
parser.add_argument('-o','--one', action='store_true', help='Move the most recently downloaded file')
parser.add_argument('-u','--undo', action='store_true', help='Undo the last move')
parser.add_argument('-r','--redo', action='store_true', help='Redo the last undone move')
parser.add_argument('--range', action='store_true', help='Specify a range of files to move')
parser.add_argument('--history', action='store_true', help='Show move history')
parser.add_argument('-v','--version', action='store_true', help='Show version information')
## TODO: [1.2.0] implement `--rename=NAME` opption to rename file in destination

args = parser.parse_args()

if args.version:
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
    print(pyproject['project']['version'])
    sys.exit()

if args.range:
    mr = most_recent.find(dp)
    print(sys.argv)

if args.find:
  print(dp,mr)

if args.history:
  save_history.read()

if args.all:
  relocate.move(mr,dp,os.getcwd())
elif args.one:
  file = []
  file.append(mr[0])
  relocate.move(file,dp,os.getcwd())

if args.undo:
  relocate.undo_last_move()
elif args.redo:

  ## TODO: [1.2.0] removed support for specifying an index with "--redo"; reimplement

  # if len(sys.argv) > sys.argv.index("--redo") + 1:
  #   index = int(sys.argv[sys.argv.index("--redo") + 1])
  #   relocate.redo_previous(index)
  # else:
  relocate.redo_previous()

if not any(vars(args).values()):
  parser.print_help()