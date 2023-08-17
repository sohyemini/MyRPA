import glob
import os

path = "./"
file_list = os.listdir(path)
print(file_list)

isExist1 = os.path.exists(r"../090_Thread.py")
isExist2 = os.path.exists(r".\\")
isExist3 = os.path.exists(r".\\test.py")
print(isExist1, isExist2, isExist3)

isFile1 = os.path.isfile(r"../090_Thread.py")
isFile2 = os.path.isfile(r".\\")
print(isFile1, isFile2)

path = "./*.py"
file_list = glob.glob(path)
print(file_list)