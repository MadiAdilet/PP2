import os

path = input()

for ch in range(ord('A'), ord('Z') + 1):
    file_path = os.path.join(path, f"{chr(ch)}.txt")  
    with open(file_path, 'w') as file:
        pass  

