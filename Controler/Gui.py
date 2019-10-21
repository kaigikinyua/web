from DB import *
from tkinter import *
from tkinter import filedialog
import os
import subprocess
from subprocess import *
import  signal
import threading
#local files import
from Files import *
from network import *
class Gui():
	def __init__(self):
		self.server=False
		self.buttons={}
		self.root=Tk()
		self.root.title("Share Server!!")
		#frames
		logoFrame=Frame(self.root,width=100)
		controlFrame=Frame(self.root)
		self.detailsFrame=Frame(self.root)
		
		#pictures
		n=Network()
		ip=n.getIp()
		IP=Label(logoFrame,text=ip,fg='red')
		IP.pack()
		logo=PhotoImage(file='./CImages/logo.png')
		logoLabel=Label(logoFrame,image=logo)
		logoLabel.pack()
		
		#buttons
		self.buttons["runserver"]=Button(controlFrame,text="Runserver",command=self.startThread)
		stopserverBtn=Button(controlFrame,text="Stop Server",command=self.stopserver)
		addFile=Button(controlFrame,text="Share File",command=self.addFile)
		self.buttons["runserver"].pack(fill=X)
		stopserverBtn.pack(fill=X)
		addFile.pack(fill=X)
		#ListBox
		self.loadList()
		removeFile=Button(self.detailsFrame,text="Hide File",command=self.removeFile)
		removeFile.pack(side=BOTTOM,fill=X)
		#packing frames
		logoFrame.pack(side=TOP)
		controlFrame.pack(side=LEFT)
		self.detailsFrame.pack(side=RIGHT)
		self.root.resizable(False,False)
		self.root.mainloop()
	def loadList(self):
		self.sharedFiles=Listbox(self.detailsFrame,width=60)
		#get shared Items and add them
		d=DB()
		items=d.showAllFiles()
		j=0
		array=["videos","pictures","others"]
		for item in array:
			for file in items:								
				self.sharedFiles.insert(j,file[1])
				j+=1
		self.sharedFiles.pack()
	def runserver(self):
		#change directoy to Server
		if self.server==False:
			self.server=True
			print("Server procees {}".format(os.getpid()))
			self.buttons["runserver"].configure(bg="green",text="Server Running")
			self.server=os.getpid()
			serverCommand="nodemon Server/mainserver.js"
			error=os.system(serverCommand)
			if(error):
				print("failed")

	def startThread(self):
		self.t=threading.Thread(target=self.runserver,name="server",args=())
		self.t.start()
	def stopserver(self):
		print(self.server)
		os.kill(self.server,signal.SIGKILL)
	def addFile(self):
		newfilepath=filedialog.askopenfilename()
		if(len(newfilepath)>0 and newfilepath!=" "):
			F=Files()
			element=F.fileExtension(newfilepath);
			if element=="directory":
				print("Adding Directory")
			else:	
				filename=F.getFilename(newfilepath)
				d=DB()
				d.addFile(newfilepath,filename,element)
				s=self.sharedFiles.size()
				self.sharedFiles.insert(s,filename)
		else:
			print("Empty")
		#F.copyFile(newfilepath,'./Server/Shared/'+element)
		#F.appendJson(element,"name",filename,'./AppData/shared.json')
	def removeFile(self):
		a=self.sharedFiles.curselection()
		if len(a)!=0:
			print(a)
			print(self.sharedFiles.get(int(a[0])))
			db=DB()
			db.hideFile(self.sharedFiles.get(int(a[0])))
			e=Errors()
			e.consoleError("File"+self.sharedFiles.get(int(a[0]))+" has been hidden")
			self.sharedFiles.delete(a)
		else:
			e=Errors()
			e.consoleError('Error')
g=Gui()
