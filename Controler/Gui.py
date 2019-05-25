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
		self.root=Tk();
		self.root.title("Share Server!!")
		self.runserverBtn=Button(self.root,text="Runserver",command=self.startThread)
		self.runserverBtn.pack()
		stopserverBtn=Button(self.root,text="Stop Server",command=self.stopserver)
		stopserverBtn.pack()
		addFile=Button(self.root,text="Share File",command=self.addFile)
		addFile.pack()
		self.root.mainloop()

	def runserver(self):
		#change directoy to Server
		os.chdir('../Server')
		print("Server procees {}".format(os.getpid()))
		self.server=os.getpid()
		serverCommand="node mainserver.js"
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
		F.appendJson(element,"name",newfilepath,'../Server/AppData/shared.json')
g=Gui()
