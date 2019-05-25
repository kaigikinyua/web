from tkinter import *
from tkinter import filedialog
import os
import subprocess
from subprocess import *
import  signal
import threading

from Files import *
class Gui():
	def __init__(self):
		self.server=False
		self.buttons={}
		self.root=Tk();
		self.root.title("Share Server!!")
		self.buttons["runserver"]=Button(self.root,text="Runserver",command=self.startThread)
		self.buttons["runserver"].pack()
		stopserverBtn=Button(self.root,text="Stop Server",command=self.stopserver)
		stopserverBtn.pack()
		addFile=Button(self.root,text="Share File",command=self.addFile)
		addFile.pack()
		self.root.mainloop()

	def runserver(self):
		#change directoy to Server
		if self.server==False:
			self.server=True
			print("Server procees {}".format(os.getpid()))
			self.buttons["runserver"].configure(bg="green",text="Server Running")
			self.server=os.getpid()
			serverCommand="node Server/mainserver.js"
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
		F=Files()
		element=F.fileExtension(newfilepath);
		filename=F.getFilename(newfilepath)
		F.copyFile(newfilepath,'./Server/Shared/'+element)
		F.appendJson(element,"name",filename,'./AppData/shared.json')
g=Gui()
