#error handling & logging
import traceback
import sys
import logging
#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger(__name__)

import os
from os import path

#import zipfile

#file & folder copying
import shutil

#time and date functions
import time
import datetime
from datetime import date, time, timedelta
import time

def main():

    #Set time variables for current time
    today = datetime.date.today()
    moment = datetime.datetime.now().time()
    now = datetime.datetime.combine(today, moment)

    #set source folder and destination folder
    src_folder =   ('source location goes here')
    dest_folder = ('dest folder goes here')

    #file to be backed-up
    filename = ('file.txt goes here')

    #set source folder and destination folder
    src_full_path =   (src_folder + filename)
    dest_full_path = (dest_folder + filename)




#tries to copy file. If it fails, it displays the error.

            #need to create a reusable def with below def.
            #def copyFile(src_full_path, dest_full_path):

    try:
    #copy source file to destination folder keeping same name
        shutil.copyfile(src_full_path, dest_full_path, follow_symlinks=True)
    # eg. src and dest are the same file
    except shutil.Error as e:
        error = ('Error: %s' % e)
        print ('removing copied file')
    # eg. source or destination doesn't exist
    except IOError as e:
        error = ('Error: %s' % e.strerror)
        print ('removing copied file')
    except OSError(FileExistsError):
        print ('removing copied file')



    # Gets and formats the backup time of the file.
    timestamp = (now.strftime("%m%d%Y-%H%M%S"))
        
    #Gets file modification time.
    #modifiedTime = (datetime.datetime.fromtimestamp(path.getmtime(src_full_path)))
    #timestamp = (modifiedTime.strftime("%m%d%Y-%H%M%S"))

    #rename file with backup time
    prevName = dest_full_path
    newName = dest_full_path.replace('.kdbx','')
    os.rename(prevName, newName+"_"+timestamp + ".kdbx")
    print(timestamp)

if __name__ == "__main__":
    main()