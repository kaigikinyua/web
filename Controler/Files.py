import json
import shutil
import os
from Errors import *
class Files:
	#read the json files
	def readJson(self,filename):
		try:
			with open(filename,'r') as file:
				data=json.load(file)
				file.close()
				return data
		except:
			e=Errors()
			e.consoleError("Failed to read "+filename)
			return False

	def writeToJson(self,filename,data):
		try:
			with open(filename,'w') as file:
				json.dump(data,file)
				file.close()
				return True
		except:
			e=Errors()
			e.consoleError("Failed to write to  "+filename)

	def appendJson(self,element,index,newData,filename):
		F=Files()
		data=F.readJson(filename)
		if data==False:
			e=Errors()
			e.consoleError("Failed to read "+filename)
			return False
		else:
			data[element]+=[{index:newData}]
			try:
				with open(filename,'w') as file:
					json.dump(data,file)
					return True
			except:
				e=Errors()
				e.consoleError("Failed to append to  "+filename)
				return False
	
	def deleteJsonElement(self,fieldname,parameter,JsonData):
		newJson=[]
		if len(JsonData)!=0:
			for item in JsonData:
				if item[fieldname]!=parameter:
					newJson+=[{fieldname:item[fieldname]}]
			return newJson
		else:
			e=Errors()
			e.consoleError("The JsonData is null")
			return False
	#Files to be Shared Utility Functions
	def ifFileExists(self,filename):
		file="./"+filename
		if os.path.isfile(file)==False:
			try:
				f=open(filename,"w")
				f.close()
				return True
			except:
				e=Errors()
				e.consoleError("Failed to create "+filename)
				return False
	def fileExtension(self,filename):
		ext=filename.split('.')
		print(ext)
		F=Files()
		d=F.readJson('./Config/ExtConfig.json')
		array=["videos","documents","pictures","others"]
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
	def getFilename(self,filepath):
		file=filepath.split('/')
		filename=file[len(file)-1]
		return filename
	#this needs to be a thread
	def copyFile(self,origin,destination):
		try:
			shutil.copy(origin,destination)
		except:
			e=Errors()
			e.consoleError("Failed to copy file "+origin+" to "+destination)
	#def deleteFile(self)
#EOF!!!------
#myJsonData=[{"name":"Kinyua"},{"name":"Antony"},{"name":"Kaigi"}]
#F=Files()
#x=F.deleteJsonElement("name","Antony",myJsonData)
#print(x)