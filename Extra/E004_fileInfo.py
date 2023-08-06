from os import path
import datetime

file = r"./E004_fileInfo.py"
ctime = path.getctime(file)  # Creating time
mtime = path.getmtime(file)  # Modify time
atime = path.getatime(file)  # Access time
size = path.getsize(file)    # File size

print(ctime)
print(datetime.datetime.fromtimestamp(ctime))
print(datetime.datetime.fromtimestamp(mtime))
print(datetime.datetime.fromtimestamp(atime))
print(size)