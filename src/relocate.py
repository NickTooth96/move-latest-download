import os
import shutil
import src.save_history as save_history
import src.check as check
import csv

APPROVE = ['Yes','yes','Y','y']
DISAPPROVE = ['No','no','N','n']


def move(newest,download_path,target_directory):
   if not check.duplicate(newest,target_directory):
      for file in newest:
         shutil.move(os.path.join(download_path,file), os.path.join(target_directory,file))
         save_history.log(file, "move", download_path, target_directory)

def undo_last_move():
   success = False
   file_list = save_history.get_last_move()

   while not success:
      file = file_list.pop()

      if os.path.exists(os.path.join(file['target directory'],file['file'])):         
         user_command = input(f"Move {file['file']} back to {file['source directory']}?\n[Y/n] ")
         
         if user_command in APPROVE:
            try:
               shutil.move(os.path.join(file['target directory'],file['file']),os.path.join(file['source directory'],file['file']))
               save_history.log(file['file'], "undo move", file['target directory'], file['source directory'])
               success = True
            except:
               success = False
         elif user_command in DISAPPROVE:
            break
         else:
            success = False

def redo_previous(range=10):
   print(range)
   print("here")