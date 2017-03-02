#!/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python archelec2.py


#
# Libs
#

import os
import shutil


#
# Config
#

folder_separator = '/'


#
# Functions
#

def archelec2() :
	path = '/Users/anne.lhote/Downloads/EL085_P_1974_Anne'
	# Iterate over folders
	os.chdir(path)
	for folder in os.listdir(path) :
		if folder != '.DS_Store' :
			folder_new_name = '_'.join(folder.split('_')[0:4])
			os.rename(folder, folder_new_name)
			for folder2 in os.listdir(folder_new_name) :
				if folder2 != 'PDF' :
					if os.path.isdir(folder_new_name + folder_separator + folder2) :
						shutil.rmtree(folder_new_name + folder_separator + folder2)
					else :
						os.remove(folder_new_name + folder_separator + folder2)
				else :
					for folder3 in os.listdir(folder_new_name + folder_separator + folder2) :
						src = folder_new_name + folder_separator + folder2 + folder_separator + folder3
						dest = folder_new_name + folder_separator + folder3
						shutil.copyfile(src, dest)
					shutil.rmtree(folder_new_name + folder_separator + folder2)


#
# Main
#
if __name__ == '__main__' :
	print 'Start script'
	archelec2()
	print 'End script'