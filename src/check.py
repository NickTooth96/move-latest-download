import os
import shutil
import src.save_history as save_history
import src.download_path as download_path
import csv


def duplicate(newest,target_directory):
   dir_list = os.listdir(target_directory)
   for file in newest:
      if file in dir_list:
         replace = info(file,dir_list,target_directory)
         if replace in ['Y','y','Yes','yes']:
            return False
         else:
            return True
   return False

def info(file,list,target_path):
   new_file_stats = os.stat(os.path.join(download_path.find(),file))
   old_file_stats = os.stat(os.path.join(target_path,file))
   print(f"\nDuplicate file found:\nFile to move: {file} | {new_file_stats.st_size}" + 
            f"\nFile in target directory: {file} | {old_file_stats.st_size}")
   replace = input("\nReplace file in target: [Y/n] ")
   return replace