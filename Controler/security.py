#list of forbidden directories in windows,linux and mac
import sqlite3
from messages import *
class Secure:
    def forbiddenDir(self):
        print("List Of Secured Directories")
    def connectDb(self,dbPath):
        try:
            self.db=sqlite3.connect(dbPath)
        except:
            e=Messages('error','Error While Making Connection To Db,\nPlease try again latter')
    def addForbidden(self,filepath):
        self.connectDb('./Config/Security.db')
        c=self.db.cursor()
        sql="INSERT INTO forbiddenfiles(path),VALUES("+filepath+");"
        try:
            c.execute(sql)
            c.commit()
        except:
            e=Messages('error','Error while securing file\n'+filepath)
