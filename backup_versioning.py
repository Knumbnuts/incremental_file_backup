import os
from os import path
#import zipfile
import shutil
import time
import datetime
from datetime import date, time, timedelta
import time

def main():
        
    #copy to backup folder
    src_file =   ('c:\\Users\\Home\\Dropbox\\Private\\keepass\\kpdb.kdbx')
    dest_file = ('d:\\BACKUPS\\keepass\\kpdb.kdbx')

    shutil.copyfile(src_file, dest_file, follow_symlinks=True)

    # Get the modification time
    t = time.ctime(path.getmtime("c:\\Users\\Home\\Dropbox\\Private\\keepass\\kpdb.kdbx"))

    modifiedTime = (datetime.datetime.fromtimestamp(path.getmtime("c:\\Users\\Home\\Dropbox\\Private\\keepass\\kpdb.kdbx")))
    timestamp = (modifiedTime.strftime("%m-%d-%Y-%H%M%S"))
    print(timestamp)

    #rename file with backup time
    prevName = 'D:\\BACKUPS\\keepass\\kpdb.kdbx'
    newName = 'D:\\BACKUPS\\keepass\\kpdb'
    os.rename(prevName, newName+"_"+timestamp + ".kdbx")

if __name__ == "__main__":
    main()