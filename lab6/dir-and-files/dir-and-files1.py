import os

path = input("")

if os.path.exists(path):
    print("Directories:", [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
    print("Files:", [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    print("All:", os.listdir(path))
else:
    print("The specified path does not exist.")
    
