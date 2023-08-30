import os
import shutil
import src.save_history as save_history
import csv


def move(file,download_path,target_directory):
   shutil.move(os.path.join(download_path,file), os.path.join(target_directory,file))
   save_history.log(file, "move", download_path, target_directory)

def undo_last_move():
   max_timestamp = 0.00
   data = save_history.load()
   print(type(data))
   for row in data:
      if max_timestamp > int(row['timestamp']):
         max_timestamp = row['timestamp']
   print(max_timestamp)
   
   # save_history.log(file, "undo_last_move", download_path, target_directory)