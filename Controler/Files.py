import json
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

f=Files()
mydata=f.readJson('jsonTrial.json')
print(mydata)
f.appendJson('names','name','james','jsonTrial.json')
mydata=f.readJson('jsonTrial.json')
print(mydata)
