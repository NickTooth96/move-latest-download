import os
import platform

dirpath = os.getcwd()
system = platform.system()
newest_download = ""

downloads_path = {"Linux" : os.path.expanduser('~'), 
                  "Windows": "'C:\'"}

dir_list = os.listdir(downloads_path[system])


for file in dir_list:
   print(file,type(file))
   if not os.path.isdir(os.path.join(downloads_path[system],file)):
      ct = os.path.getctime(os.path.join(downloads_path[system],file))
      if ct < os.path.getctime(os.path.join(downloads_path[system],newest_download)) or newest_download == "":
         newest_download = file

print(newest_download)
