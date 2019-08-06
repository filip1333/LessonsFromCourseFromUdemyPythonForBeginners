import os
import time

dir = input("Enter file directory: ")

if not os.path.isdir(dir):
    print("%s must be a directory" % dir)

else:
    file = input("Enter the file name: ")
    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print('File %s does not exist!' % path)

    else:
        print("This information about file %s" % path)
        print("The last modification:", time.localtime(os.path.getmtime(path)))
        print("File size:", os.path.getsize(path))
        print("File location:", os.getcwd())
        print("Relative path to the file is:", os.path.realpath(path))
