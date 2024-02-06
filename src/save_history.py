import os
import io
import time
import csv
import datetime

filepath = os.path.realpath(os.path.dirname(__file__))[:-4]
PATH = os.path.join(filepath,'data','data.csv')
DATA_ERROR_MSG = "Data file not found in" + PATH + "\nCreate file [Y/n] "

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
    try:
        reader = csv.DictReader(open(PATH))
    except:
        ans = input(DATA_ERROR_MSG)
        if ans in ["Y","y"]:
            create_data_file()
    return reader

def load_list():
    out_list = []
    reader = csv.DictReader(open(PATH))
    for row in reader:
        out_list.append(row)
    return out_list

def get_move_list():
    max_timestamp = "0"
    out_list = []
    data = load()
    for row in data:
        mt = float(max_timestamp)
        t = float(row['timestamp'])
        if mt < t:
            if row['operation'] == "move":            
                max_timestamp = row['timestamp']
                out_list.append(row)
    return out_list

def create_data_file():
    print(filepath)
    os.mkdir(os.path.join(filepath, 'data'))
    # os.makedirs(os.path.dirname(os.path.join(filepath, 'data')), exist_ok=True)
    with open(PATH,'x') as file:
        file.write('timestamp,file,operation,source directory,target directory\n')
    