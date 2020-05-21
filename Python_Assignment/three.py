"""
					Assignment 3:
Create a function which lists all the files in current directory.
Create another function to verify whether current python program file (.py) is listed in the above returned list of files.
Modify first function to accept two arguments, first – path to list the files from,
second – filter to limit the specific extension files 
(i.e. function(“c:\test”, “*.txt”) should list all *.txt files from c:\test directory.)
"""

import os

# function for displaying particular path and containing files
def dirlist(path,filter):  
    dir_list = []
    is_file_found = 0
    
    for file in os.listdir(path):
        if file.endswith(filter):
            is_file_found = 1
            # Prints the file name which are ending with given in filter
            print(os.path.join(path, file))  
    
    # If file not found then 
    if is_file_found != 1:  
        print("No file found in this directory")
        
    dir_list.append(os.listdir(path))
    os.chdir(path)
    return dir_list

# This function checks if the currently working file is in file list or not
def checkfile(current_file, directory_list):  
  
    # for loop is for list to find if the current working file is in this directory list or not 
    for i in range(len(directory_list)):  
   
        if current_file in directory_list[i]:
                print("\nCurrent working file is in list (", current_file, ")")
        else:
                print("\nCurrent working file doesn't exists in this list")
      


path = input("\nEnter file path")
filter = input("\nEnter file extension")  # getting extension from user
directory_list = dirlist(path, filter)  # calling dirlist function and search for that ending extemsion file
# print(type(directory_list))     #uncomment for checking the type of directory_list
current_file = os.path.basename(__file__)  # getting current working file name
checkfile(current_file, directory_list)     