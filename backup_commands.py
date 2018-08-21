import os
import zipfile
import shutil
import time
import datetime

from datetime import date
from datetime import time
from datetime import datetime
from os import path

def main():
    t = time.ctime(path.getmtime("c:\\Users\\Home\\Dropbox\\Private\\keepass\\kpdb.kdbx"))
    print(t)
    #print(datetime.datetime.fromtimestamp(path.getmtime("guru99.txt.bak")))

    today = datetime.date.today()
    moment = datetime.datetime.now().time()
    now = datetime.datetime.combine(today, moment)

    #copy to backup folder
    src_file =   ('c:\\Users\\Home\\Dropbox\\Private\\keepass\\kpdb.kdbx')
    dest_file = ('d:\\BACKUPS\\keepass\\kpdb.kdbx')
    shutil.copyfile.(src_file, dest_file, follow_symlinks=True)
        
    #get time of backup file
    modifiedTime = os.path.getmtime(src_file)
    
    #variable out time
    timestamp = datetime.datetime(modifiedTime.strftime("%b-%d-%Y_%H.%M.%S"))
    #rename file with backup time
    prevName = 'D:\\BACKUPS\\keepass\\kpdb.kdbx'
    newName = 'D:\\BACKUPS\\keepass\\'
    os.rename(prevName, newName+"_"+timestamp + ".kdb")
    print(newName)
    
    
    
    
    #copy files to a target folder
    if __name__ == "__main__":
        main()