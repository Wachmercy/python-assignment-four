with open("python.txt", "r") as infile:
    content = infile.read()
modified_content = content.lower()
with open("xyz.txt", "w") as outfile:
    outfile.write(modified_content)

filename = input("Enter the filename : ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:\n")
        print(content)

except FileNotFoundError:
    print("The file does not exist,recheck the filename.")
