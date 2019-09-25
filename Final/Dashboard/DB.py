import sqlite3
from Messages import *
class DB:
    def __init__(self):
        try:
            self.db=sqlite3.connect('../AppData/DB/share.db')
        except:
            m=Messages('error','Error While Connecting To Database')
    def addFile(self,path,filename,videotype):
        sql="INSERT INTO sharedfiles (path,filename,filetype) VALUES('"+path+"','"+filename+"','"+videotype+"');"
        print(sql)
        c=self.db.cursor()
        c.execute(sql)
        self.db.commit()
        print(sql)
        #except:
        #    m=Messages('Error','Error While Sharing File')
    def showAllFiles(self):
        sql="SELECT * FROM sharedfiles;"
        c=self.db.cursor()
        c.execute(sql)
        data=c.fetchall()
        return data

    def dbAdmin(self,sql):
        #sql="CREATE TABLE sharedfiles (path varchar(50) not null,filename varchar(50) not null,filetype varchar(50));"
        c=self.db.cursor()
        c.execute(sql)
        self.db.commit()

    def hideFile(self,filename):
        sql="DELETE FROM sharedfiles where filename='"+filename+"';"
        c=self.db.cursor()
        c.execute(sql)
        self.db.commit()