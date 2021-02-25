from tkinter import *
from tkinter import filedialog
import threading
from Files import *
from DB import *
from Messages import *
from network import *
import os
class Gui:
    def __init__(self):

        self.root=Tk()
        i=Network()
        ip=i.getIp()
        self.root.title("WebShare running on "+ip)
        
        self.utilityPanel=Frame(self.root)
        self.createLabel(self.utilityPanel,'Hello There!!')
        logo=PhotoImage(file='../AppData/Images/logo.png')
        l=Label(self.utilityPanel,image=logo)
        l.pack()
        self.createButton(self.utilityPanel,'Start Server',self.runserver)
        self.createButton(self.utilityPanel,'Share File',self.addFile)
        self.utilityPanel.pack(side=LEFT,fill=Y)

        self.packPanel=Frame(self.root)
        self.createLabel(self.packPanel,'Shared Files')
        self.fileList=Listbox(self.packPanel,height=17,width=50)
		#get shared Items and add them
        d=DB()
        items=d.showAllFiles()
        array=["videos","pictures","audio","compressed","others"];j=0;
        for item in items:								
        	self.fileList.insert(j,item[1])
        	j+=1

        self.fileList.pack(fill=X)
        self.createButton(self.packPanel,'Hide File',self.removeFile)
        self.packPanel.pack(side=RIGHT,fill=Y)
        self.root.resizable(False,False)
        self.root.mainloop()
    #simplifying things
    #Gui simplification
    def createButton(self,attach,button,method):
        button=Button(attach,text=button,command=method)
        button.pack(fill=X)
    def createLabel(self,attach,label):
        l=Label(attach,text=label)
        l.pack()
    

    def runserver(self):
        t1=threading.Thread(target=self.server,name="serverthread",args=())
        t1.start()

    def server(self):
        os.chdir('../Server')
        serverCommand="nodemon index.js"
        error=os.system(serverCommand)
        if error:
            print("Error "+error)

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
    			s=self.fileList.size()
    			self.fileList.insert(s,filename)
    	else:
    		print("Empty")
    	#F.copyFile(newfilepath,'./Server/Shared/'+element)
    	#F.appendJson(element,"name",filename,'./AppData/shared.json')
    def removeFile(self):
        a=None
        try:
    	    a=self.fileList.curselection()
        except:
            Messages('error',"Please Select A File")
        if len(a)!=0 or a!=None:
            print(a)
            filename=self.fileList.get(int(a[0]))
            print(filename+" File name ")
            db=DB()
            db.hideFile(self.fileList.get(int(a[0])))
            Message('error',filename+" has been hidden")
            self.fileList.delete(a)
c=Gui()
