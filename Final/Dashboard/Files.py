import json
import shutil
import os
from Messages import *
from DB import *
class Files:
	#Files to be Shared Utility Functions
	def readJson(self,filename):
		try:
			with open(filename,'r') as file:
				data=json.load(file)
				file.close()
				return data
		except:
			Messages('error','Could Not read '+filename)
			return False

	def ifFileExists(self,filename):
		file="./"+filename
		if os.path.isfile(file)==False:
			try:
				f=open(filename,"w")
				f.close()
				return True
			except:
				Messages('error','Error While Opening File'+filename)
				return False
	def fileExtension(self,filename):
		if os.path.isdir(filename):
			print("File is directory")
			return "directory"
		else:	
			ext=filename.split('.')
			print(ext)
			F=Files()
			d=F.readJson('../AppData/Config/ExtConfig.json')
			array=["videos","audio","documents","text","pictures","compressed","others"]
			for element in array:
				i=0;print(element)
				while(i<(len(d[element])-1)):
					print(d[element][i]["ext"])
					if(ext[len(ext)-1]==d[element][i]["ext"]):
						print(filename +" is belongs to "+element)
						fileElement=element
						return element
					i+=1
				print("\n")
			fileElement="others"
			return fileElement
	def addDirectory(self,directory):
		files=os.listdir(directory)
		for file in files:
			if os.path.isfile(directory+"/"+file):
				filename=self.getFilename(directory+"/"+file)
				extension=self.fileExtension(directory+"/"+file)
				d=DB()
				d.addFile(directory+"/"+file,filename,extension)
	def getFilename(self,filepath):
		file=filepath.split('/')
		filename=file[len(file)-1]
		return filename

	def filePathIsFile(self,filepath):
		if os.path.isfile(filepath):
			return True
		else:
			if os.path.isdir(filepath):
				return "dir"
			else:
				return False
