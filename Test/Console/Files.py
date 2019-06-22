import os
import json
class Files():
    def filePath(self,filepath):
        rootPath=filepath.split('/')
        root='/'+rootPath[1]+'/'+rootPath[2]
        #analyze file path and if is video/audio or document
        self.fileExtension(filepath)
        print(root)
    def fileExtension(self,filePath):
        #check if file is a dir
        fileExt=filePath.split('.')
        ext= fileExt[1]
        print(ext) 
F=Files()
F.filePath('/run/media/antony/New Volume/iHuB/MyZone/Share.exe')