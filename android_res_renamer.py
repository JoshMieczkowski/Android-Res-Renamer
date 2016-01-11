import os, sys, re
from Tkinter import Tk
from tkFileDialog import askdirectory 

Tk().withdraw()
folder_path = askdirectory()

for root, dirs, files in os.walk(folder_path):
	for file in files:
		newFileName = file.lower()
		newFileName = newFileName.replace('-', '_')
		newFileName = newFileName.replace(' ', '_')
		newFileName = re.sub('[^a-z0-9/_/.]+', '', newFileName)
		
		oldFilePath = os.path.join(root, file)
		newFilePath = os.path.join(root, newFileName)
		
		os.rename(oldFilePath, newFilePath)
