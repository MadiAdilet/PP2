import os

path = input("Enter the path to the file: ")
if os.path.isfile(path) and os.access(path, os.W_OK):
    os.remove(path)
    print("File deleted.")
else:
    print("Error: Unable to delete file.")