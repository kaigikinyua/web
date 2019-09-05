from tkinter import messagebox
class Messages:
    def __init__(self,msgtype,msg):
        msgtype=msgtype.lower()
        if(msgtype=='error'):
            messagebox.showerror(title='Error',message=msg)
            
        
