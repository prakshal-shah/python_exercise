"""
					Assignment 3:
Create a function which lists all the files in current directory.
Create another function to verify whether current python program file (.py) is listed in the above returned list of files.
Modify first function to accept two arguments, first – path to list the files from,
second – filter to limit the specific extension files 
(i.e. function(“c:\test”, “*.txt”) should list all *.txt files from c:\test directory.)
"""



import os
os.chdir(r"C:\Users\prakshal.shah\eclipse-workspace")  # Changed directory for listing all directory


def dirlist(path,filter):  # function for displaying particular path and containig files
    dir_list = []
    is_file_found = 0
    
    for file in os.listdir(path):
        if file.endswith(filter):
            is_file_found = 1
            print(os.path.join(path, file))  # Prints the file name which are ending with given in filter
    if is_file_found != 1:  # If file not found then 
        print("No file found in this directory")
       
    dir_list.append(os.listdir(path))
    os.chdir(path)
    return dir_list


def checkfile(current_file, directory_list):  # This function checks if the currently working file is in file list or not
  
    for i in range(len(directory_list)):  # for loop is for list to find if the current working file is in this directory list or not 
   
        if current_file in directory_list[i]:
                print("\nCurrent working file is in list (", current_file, ")")
        else:
                print("\nCurrent working file doesn't exists in this list")
      

print(os.listdir())
while True:
    path = input("\nEnter file path")
  # try and catch if user enter wrong directory then program will not terminate
    try:
        print(os.listdir(path))
        break
    except FileNotFoundError:
        print("No such directory")

filter = input("\nEnter file extension")  # getting extension from user
directory_list = dirlist(path, filter)  # calling dirlist function and search for that ending extemsion file
# print(type(directory_list))     #uncomment for checking the type of directory_list
current_file = os.path.basename(__file__)  # getting current working file name
checkfile(current_file, directory_list)     
