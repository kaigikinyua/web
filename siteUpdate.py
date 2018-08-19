import os
class Copy:
    #method that list what is in the directory
    def dir(self):
        os.system("ls /home/antony/Music> dir.txt")
        os.system("touch myfile.html")
    #method that adds the data to the indexfile in www/html
    def add(self):
        #file=open("/var/www/html/WShare/index.html","r")
        file=open("dir.txt")
        values=file.readlines();
        file.close()
        data=[]
        a=Copy()
        f_values=a.removenewLine(values)
        for v in f_values:
            data+=["<div><video height='100px' width='100px' controls src='"+v+"'/></div>"]
            #print data
        file=open("myfile.html","w")
        file.write("<html>\n\t<head>\n\t\t<title></title></head><body>")
        file.close()
        file=open("myfile.html","a")
        for d in data:
            file.write("\t"+d+"\n")
        file.close()
    def removenewLine(self,data):
        sifted=[]
        for v in data:
            sifted_e=""
            for c in v:
                if c !="\n":
                    sifted_e=sifted_e + c
            sifted+=[sifted_e]
        print sifted
        return sifted
c=Copy()
c.dir()
c.add()