import os
def path_info(path):
    if os.path.exists(path):
        print("File name:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")
path=input()
path_info(path)