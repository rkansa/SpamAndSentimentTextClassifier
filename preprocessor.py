__author__ = 'raj'

import glob
import os
import sys
directory=sys.argv[1]
training=sys.argv[2]
trainingFIle=open(training,"w")

inputDir=glob.glob(directory)
filenames=[]
for file in inputDir:
    fileName=os.path.split(file)[1]
    dir=os.path.split(file)[0]
    filenames.append(dir+"/"+fileName)
filenames=sorted(filenames)

for file in filenames:
    fileName= os.path.split(file)[1]
    label=fileName.split(".")[0]
    trainingFIle.write(label+" ")
    fileHandle=open(file,"r",errors='ignore')
    fileContents=fileHandle.readlines()
    for message in fileContents:
      message=message.rstrip("\n")
      trainingFIle.write(message+" ")
    trainingFIle.write("\n")

trainingFIle.close()