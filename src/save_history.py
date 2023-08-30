import os
import io
import time
import csv

PATH = 'data/.data.csv'

def log(file, operation, download_path, current_working_directory):
    data = io.StringIO()
    if not os.path.isfile(PATH):
        data.write('timestamp, file, operation, source directory, target directory\n')
        
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
