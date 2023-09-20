import os


def find(download_path: str, range=300):
   """ Returns a list of the most recently downloaded files. Uses the range variable to check for 
   multiple consecutive downloads. The default range is five minutes. When several file are 
   downloaded within five minutes of each other they are all added to the output list to be moved.
   If no other downloads are found to be downloaded within five minutes of the most recent download
   then the output list will only contain one item.  

   Args:
       download_path (str): path to user's 'Downloads' directory from download_path.find() 
       range (int, optional): Range of time within which to find downloads. Defaults to 300 seconds.

   Returns:
       newest_downloads (list): list containing all the most recent downloads 
   """
   newest_download = ""
   newest_downloads = []
   dir_list = os.listdir(download_path)

   for file in dir_list:
      if not os.path.isdir(os.path.join(download_path,file)):
         ct = os.path.getctime(os.path.join(download_path,file))
         if ct > os.path.getctime(os.path.join(download_path,newest_download)) or newest_download == "":
            newest_download = file

   newest = os.path.getctime(os.path.join(download_path,newest_download))
   for file in dir_list:
      if not os.path.isdir(os.path.join(download_path,file)) and not file in newest_downloads:
         ct = os.path.getctime(os.path.join(download_path,file))
         if ct > newest - range:
            newest_downloads.append(file)
   
   return newest_downloads