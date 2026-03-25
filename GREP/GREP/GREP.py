file_name = input("Enter the file name: ")
pattern = input("Enter the pattern: ")

file = open(file_name, "r")
lines = file.readlines()
file.close()

for line in enumerate(lines):
    if pattern in line:
        print(file_name,i+1, line.strip())
