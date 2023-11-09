import datetime
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
   file_list = save_history.get_move_list()

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

def redo_previous(end_range=10):
   history = save_history.load_list()
   for item in history[len(history) - end_range:len(history)]:
      date = str(datetime.datetime.fromtimestamp(float(item['timestamp']))).split(" ")[0]
      num = history.index(item)
      dst = item['target directory']
      if "Downloads" in dst:
         dst = "Downloads"
      name = item['file']
      display = f"JOB {str(num).rjust(3,'0')}: {date} | %.20s -> {dst}" % name.ljust(20,' ')
      print(display)

   user_command = input("Choose JOB [Number] to redo\n[ENTER] to cancel: ")
   if user_command != '':
      if not os.path.exists(os.path.join(history[int(user_command)]['target directory'],history[int(user_command)]['file'])):
         move([history[int(user_command)]['file']],history[int(user_command)]['source directory'],history[int(user_command)]['target directory'])
      else:
         print("ERROR: Invalid Operation")

   
