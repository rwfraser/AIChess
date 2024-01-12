# DOTPYTODOTTXT.py
# bulk rename of .py files to .txt files so Windows Preview will work
import os
import shutil
# read all .py files into a list and then iterate 

allfiles = os.listdir()
# if 'py2txt' not in allfiles:
#	os.mkdir('py2txt')

for file in allfiles:
	if '.py' in file:
		print(f'found python source file: {file}')
		shutil.copyfile(file, file + '.txt')
		print(f'created: {file}.txt')
