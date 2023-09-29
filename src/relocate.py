import os
import shutil
import src.save_history as save_history
import src.check as check
import csv


def move(newest,download_path,target_directory):
   if not check.duplicate(newest,target_directory):
      for file in newest:
         shutil.move(os.path.join(download_path,file), os.path.join(target_directory,file))
         save_history.log(file, "move", download_path, target_directory)

def undo_last_move():
   file = save_history.get_last_move()
   shutil.move(os.path.join(file['target directory'],file['file']),os.path.join(file['source directory'],file['file']))
   save_history.log(file['file'], "undo move", file['target directory'], file['source directory'])