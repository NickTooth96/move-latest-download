#!/usr/bin/env python3

import os
import sys
import argparse
import tomllib
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate
import src.save_history as save_history


VERSION = "1.2.0"


def main(argv=None):
  if argv is None:
    argv = sys.argv[1:]

  dp = download_path.find()
  mr = most_recent.find(dp)

  parser = argparse.ArgumentParser(
    prog='mvld',
    description='Finds the most recently downloaded file/files and moves them to a specified location.',
    epilog='By Nicholas Toothaker')

  parser.add_argument('-f', '--find', action='store_true', help='Find the most recently downloaded file/files')
  parser.add_argument('-a', '--all', action='store_true', help='Move all listed files')
  parser.add_argument('-o', '--one', action='store_true', help='Move the most recently downloaded file')
  parser.add_argument('-u', '--undo', action='store_true', help='Undo the last move')
  parser.add_argument('-r', '--redo', action='store_true', help='Redo the last undone move')
  parser.add_argument('--range', action='store_true', help='Specify a range of files to move')
  parser.add_argument('--history', action='store_true', help='Show move history')
  parser.add_argument('-v', '--version', action='store_true', help='Show version information')

  args = parser.parse_args(argv)

  if args.version:
    # read version from pyproject if available, else use VERSION
    try:
      with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)
      print(pyproject['project'].get('version', VERSION))
    except Exception:
      print(VERSION)
    raise SystemExit(0)

  if args.find:
    print(dp, mr)

  if args.history:
    save_history.read()

  if args.all:
    relocate.move(mr, dp, os.getcwd())
  elif args.one:
    file = [mr[0]]
    relocate.move(file, dp, os.getcwd())

  if args.undo:
    save_history.undo(dp)
  if args.redo:
    save_history.redo(dp)

    


if __name__ == "__main__":
  main()