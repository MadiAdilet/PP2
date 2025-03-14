source_path = input("Enter the path to the source file: ")

with open(source_path, 'r') as source_file:
    content = source_file.read()

with open("file.txt", 'w') as target_file:
    target_file.write(content)

print("File contents copied successfully.")