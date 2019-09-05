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
		self.root=Tk();

		#frames
		logoFrame=Frame(self.root)
		controlFrame=Frame(self.root)
		detailsFrame=Frame(self.root)
		
		#pictures
		n=Network()
		ip=n.getIp()
		IP=Label(logoFrame,text=ip)
		IP.pack()
		logo=PhotoImage(file='./CImages/logo.png')
		logoLabel=Label(logoFrame,image=logo)
		logoLabel.pack()
		
		#buttons
		self.root.title("Share Server!!")
		self.buttons["runserver"]=Button(controlFrame,text="Runserver",command=self.startThread)
		stopserverBtn=Button(controlFrame,text="Stop Server",command=self.stopserver)
		addFile=Button(controlFrame,text="Share File",command=self.addFile)
		self.buttons["runserver"].pack()
		stopserverBtn.pack()
		addFile.pack()
		#ListBox
		self.sharedFiles=Listbox(detailsFrame,width=50)
		#get shared Items and add them
		d=DB()
		items=d.showAllFiles()
		j=0;
		array=["videos","documents","pictures","others"]
		for item in array:
			for file in items:								
				self.sharedFiles.insert(j,file[1])
				j+=1
		self.sharedFiles.pack()


		#packing frames
		logoFrame.pack(side=TOP)
		controlFrame.pack(side=LEFT)
		detailsFrame.pack(side=RIGHT)
		self.root.resizable(False,False)
		self.root.mainloop()

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
			filename=F.getFilename(newfilepath)
			d=DB()
			d.addFile(newfilepath,filename,element)
		else:
			print("Empty")
		#F.copyFile(newfilepath,'./Server/Shared/'+element)
		#F.appendJson(element,"name",filename,'./AppData/shared.json')

g=Gui()
