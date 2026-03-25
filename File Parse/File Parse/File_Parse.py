file_name = input("Enter the file name to parse: ")

file = open(file_name, "r")

word = input("Enter the word to count: ")

count = 0

line = file.readline()

while line:
    if word in line:
        count += 1
    line = file.readline()

count = 0

print(f"Searching for '{word}' in '{file_name}'")
print(f"The word '{word}' appears {count} times in the file '{file_name}'.")