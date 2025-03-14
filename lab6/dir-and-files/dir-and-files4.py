import os
def count_lines(file):
    if not os.path.exists(file):
        print("File not found!")
        return

    with open(file, "r", encoding="utf-8") as f:
        print("Line count:", len(f.readlines()))
file = input("Enter file path: ")
count_lines(file)