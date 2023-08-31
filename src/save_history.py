import os
import io
import time
import csv

filepath = os.path.realpath(os.path.dirname(__file__))[:-4]
PATH = os.path.join(filepath,'data','data.csv')

def log(file, operation, download_path, current_working_directory):
    data = io.StringIO()
    if not os.path.isfile(PATH):
        data.write('timestamp,file,operation,source directory,target directory\n')
        
    data.write(str(time.time()) + ",")
    data.write(file + ",")
    data.write(operation + ",")
    data.write(download_path + ",")
    data.write(current_working_directory)
    data.write("\n")

    with open(PATH,'a') as log:
        log.write(data.getvalue())

def load():
    reader = csv.DictReader(open(PATH))
    return reader

def get_last_move():
    max_timestamp = "0"
    data = load()
    file_info = {}
    for row in data:
        mt = float(max_timestamp)
        t = float(row['timestamp'])
        if mt < t:
            if row['operation'] == "move":            
                max_timestamp = row['timestamp']
                file_info = row
    return file_info