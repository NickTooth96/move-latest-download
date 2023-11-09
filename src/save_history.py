import os
import io
import time
import csv
import datetime

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

def read():
    data = load()
    num = 1
    for row in data:
        date = str(datetime.datetime.fromtimestamp(float(row['timestamp']))).split(" ")[0]
        if "Downloads" in row['source directory']:
            src = "Downloads"
        else:
            src = row['source directory']

        if "Downloads" in row['target directory']:
            dst = "Downloads"
        else:
            dst = row['target directory']

        file = row['file']
        print(f"{str(num).rjust(3,'0')}) {date} | %.20s was moved from {src} to {dst}" % file)
        num += 1

def load():
    reader = csv.DictReader(open(PATH))
    return reader

def get_last_move():
    #TODO fix issue when more than one file moved undo can move last 
    # file back to downloads but then can't move other files 
    # because get_last_move() finds the same file again and tries to move it to downloads again.
    max_timestamp = "0"
    out_list = []
    data = load()
    file_info = {}
    for row in data:
        mt = float(max_timestamp)
        t = float(row['timestamp'])
        if mt < t:
            if row['operation'] == "move":            
                max_timestamp = row['timestamp']
                out_list.append(row)
    return out_list

def get_move_list():
    """Reads file move history
    creates list of dictionaries pointing to moved files, with source and destination
    Returns list
    """
    max_timestamp = "0"
    data = load()
    file_info = {}
    for row in data:
        mt = float(max_timestamp)
        t = float(row['timestamp'])
        print(row)
        if mt < t:
            if row['operation'] == "move":            
                max_timestamp = row['timestamp']
                file_info = row
    return file_info
    