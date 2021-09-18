
# Andrew Schaefer
# 5/6/21
# Mod 10 Assignment, Files

# Imports OS Library
import os.path
from os import path

# User input names directory.
user_directory = input('Enter the directory name: ')

# User input names file.
filename = input('\nEnter the file name: ')

# Places new file in new directory.
file_path = os.path.join(user_directory, filename)

# Checks if directory already exists. If not,
# it creates one.	
if not os.path.isdir(user_directory):
	os.mkdir(user_directory)

# Opens file in write mode and adds user input to file.
file = open(file_path, 'w')
file.write(input('\nEnter your name: '))
file.write(input('\nEnter your address: '))
file.write(input('\nEnter your phone number: '))
file.close()

# Opens file in read mode
file = open(file_path, 'r')
contents = file.read()

# Displays contents of file in a line
# seperated by commas.
print(contents.split())
file.close()







