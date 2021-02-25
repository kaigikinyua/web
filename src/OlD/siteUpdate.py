import os
import shutil
class dataTransfer:
    #takes the parameter of the directory of which folder to host
    def copy(self,dir):
        file=open("dir.txt","r")
        values=file.readlines()
        for v in values:
            os.system("cp -r "+dir+" /var/www/html/Node")
class Files:
    #method that list what is in the directory
    def dir(self,dir):
        os.system("ls -r "+dir+">dir.txt")
        os.system("touch myfile.html")

    #method that adds the data to the indexfile in www/html
    def add(self,dir):
        #file=open("/var/www/html/WShare/index.html","r")
        file=open("dir.txt")
        values=file.readlines();
        file.close()
        data=[]
        a=Files()
        f_values=a.removenewLine(values)
        folder=a.removeSlash(dir)
        for v in f_values:
            data+=["<div><video height='250px' width='300px' controls src='"+folder+"/"+v+"'/></div>"]
            #print data
        file=open("/var/www/html/Node/index.html","w")
        file.write("<html>\n\t<head>\n\t\t<title></title></head>\n\t<body><table border='0'>")
        file.close()
        file=open("/var/www/html/Node/index.html","a");i=0;j=0
        for d in data:
            if j>0 and j<4:
                file.write("\t<td>"+d+"<i>"+f_values[i]+"</i></td>\n")
                j+=1
            elif j==4:
                file.write("\t<td><td>"+d+"<i>"+f_values[i]+"</i></td></tr>\n")
                j+=1
            else:
                file.write("\t<tr><td>"+d+"<i>"+f_values[i]+"</i></td>\n")
                j=0
            j+=1
            i+=1
        file.write("</table></body></html>")
        file.close()
    def removenewLine(self,data):
        sifted=[]
        for v in data:
            sifted_e=""
            for c in v:
                if c !="\n":
                    sifted_e=sifted_e + c
            sifted+=[sifted_e]
        #print sifted
        return sifted

    def removeSlash(self,dir):
        product=""
        for c in dir:
            if c=="/":
                product=""
            else:
                product+=c
        print product
        return product
print "Enter the directory in which you want to host"
dir=raw_input()
d=dataTransfer()
c=Files()
c.dir(dir)
d.copy(dir)
c.add(dir)