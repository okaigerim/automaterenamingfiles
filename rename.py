#We need to use the OS module

import os

os.chdir(") #Set the directory with files you want to rename
print(os.getcwd()) #Check the current working directory

for file in os.listdir():
	print(f) #Print all the files and check if they are the same
	file_name, f_ext = os.path.splitext(f) #Get the name and the extension of files
	'''
	My file names look like this:
	
	Laboratory work 1.docx
	Laboratory work 2.docx
	Laboratory work 3.docx
	Laboratory work 4.docx	
	'''
	file_lab, file_work, file_num = file_name.split(' ') #Split file names and set them as variables
	#I wan to rename files as Lab 1.docx, Lab 2.docx, ... Lab N.docx
	file_lab = file_lab.strip()[:3] #I need the first name only until the third character
	
	print('{} {}{}'.format(file_lab, file_num, file_ext)) #Check if its working
	
	#Set it as a new variable
	new_name = '{} {}{}'.format(file_lab, file_num, file_ext)
	
	os.rename(file, new_name) 
	
	
