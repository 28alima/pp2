import os
#1 
def listDirectories(path):
    directories = []
    files = []

    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            directories.append(i)
        else: 
            files.append(i)

    return directories, files 
path = "D:\Презентации"
directories, files = listDirectories(path)
print("Directories:")
print(directories)
print("Files:")
print(files)



#2 
def checkAccess(path):
    if not os.path.exists(path):
        print(f"The path '{path}' doesn't exist")
        return
    if os.access(path, os.R_OK):
        print(f"The path '{path}' is readble")
    else:
        print(f"the path '{path}' isn't readble")

    if os.access(path, os.W_OK):
        print(f"The path '{path}' is writable")
    else:
        print(f"thee path '{path}' is not writable ")

    if os.path.isdir(path):
        if os.access(path, os.X_OK):
            print(f"The path '{path}' is executable")
        else:
            print(f"The path '{path}' is not executable")

    else: 
        print(f"The path '{path}' is not a directory, so executability is not applicable")

path = "D:\Essays"
checkAccess(path)



#3 
def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists")
        
        directory, filename = os.path.split(path)
        
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = "D:\SteamLibrary"
test_path(path)



#4 
def counterL(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return -1  # Если не найдет код мой файл

filename = "D:\ForLab6\ForLab6.txt" 
num_lines = counterL(filename)
if num_lines != -1:
    print(f"The number of lines in '{filename}' is: {num_lines}")



#5 
def AddList(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"The list has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = "D:\ForLab6\ForLab6.txt" 
my_list = ["bada", "dawa", "ae", "da"]
AddList(filename, my_list)



#6 
import string
def generate_text_files():
    try:
        for letter in string.ascii_uppercase:
            filename = f"{letter}.txt"
            with open(filename, 'w') as file:
                file.write(f"This is the content of {filename}.")
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_text_files()



#7 
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            contents = source.read()
        with open(destination_file, 'w') as destination:
            destination.write(contents)
        
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = "D:\ForLab6\ForLab6.txt"  
destination_file = "D:\ForLab6\Tocopy.txt"  
copy_file(source_file, destination_file)



#8 
def ToDelete(path):
    try:
        if not os.path.exists(path):
            print(f"The file '{path}' doesnt exist")
            return
        if not os.path.isfile(path):
            print(f"'{path}' is not a file")
            return
        
        if not os.access(path, os.W_OK):
            print(f"You do not have permission to delete '{path}'")
            return
        os.remove(path)
        print(f"The file '{path}' has been deleted successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

path = "D:\ForLab6\Todelete.txt"
ToDelete(path)