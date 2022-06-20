import os 

os.system("date")

# making a directory
os.mkdir("GP")

#get the current working directory
os.getcwd()

#checking path existence
import os 
path='C:\Users\VNANESWAR\Python\99'

isExists=os.path.exists(path)
print(isExists)

#root and extension
import os 
path='C:\Users\VNANESWAR\Python\99\file.txt'
root_ext=os.path.splitext(path)

print("Root path: ",root_ext[0])
print("extension path: ",root_ext[1])

os.listdir()

import os 
import shutil

path='C:\Users\VNANESWAR\Python\99'
print("Before copying file: ")
print(os.listdir(path))

source='C:\Users\VNANESWAR\Python\99\file1.txt'
destination='C:\Users\VNANESWAR\Python\99\file2.txt'

dest=shutil.copy(source,destination)

print("after copying file: ")
print(os.listdir(path))


print("Before moving file: ")
print(os.listdir(path))

source='C:\Users\VNANESWAR\Python\99\file1.txt'
destination='C:\Users\VNANESWAR\Python\99\file2.txt'

dest2=shutil.move(source,destination)

print("after moving file: ")
print(os.listdir(path))












import os
import shutil

# Write the name of the directory here,
# that needs to get sorted
# path = '/home/rajeev/Videos'
path = input("enter the name of the directory to be sorted :- ")

# This will create a properly organized
# list with all the filename that is
# there in the directory
list_of_files = os.listdir(path)

# This will go through each and every file
for file in list_of_files:
    name, ext = os.path.splitext(file)

    # This is going to store the extension type
    ext = ext[1:]

    # This forces the next iteration,
    # if it is the directory
    if ext == '':
        continue

    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    

