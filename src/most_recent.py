import os


def find(download_path):

   newest_download = ""
   dir_list = os.listdir(download_path)

   for file in dir_list:
      if not os.path.isdir(os.path.join(download_path,file)):
         ct = os.path.getctime(os.path.join(download_path,file))
         if ct > os.path.getctime(os.path.join(download_path,newest_download)) or newest_download == "":
            newest_download = file
   
   return newest_download

def find_all(download_path, range=300):

   print(f"Range: {range}s")

   newest_downloads = []
   dir_list = os.listdir(download_path)   
   newest_download = find(download_path)            
   newest_downloads.append(newest_download)
   newest = os.path.getctime(os.path.join(download_path,newest_download))
   
   for file in dir_list:
      if not os.path.isdir(os.path.join(download_path,file)) and not file in newest_downloads:
         ct = os.path.getctime(os.path.join(download_path,file))
         if ct > newest - range:
            newest_downloads.append(file)
   print(newest_downloads)
   return newest_downloads