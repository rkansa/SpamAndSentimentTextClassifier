__author__ = 'raj'

import glob
import os
import sys

directory=sys.argv[1]
print(directory)
training=sys.argv[2]
#training="spam_training.txt"
trainingFIle=open(training,"w")
#trainingFIle=open("sentiment_training.txt","w")
#directory= "/home/raj/repos/SPAM_dev/*.txt"
#directory= "/home/raj/repos/SPAM_training/*.txt"
#directory= "/home/raj/repos/SENTIMENT_training/*.txt"
inputDir=glob.glob(directory)
for file in inputDir:
    fileName= os.path.split(file)[1]
    label=fileName.split(".")[0]
    trainingFIle.write(label+" ")
    fileHandle=open(file,"r",errors='ignore')   #errors='ignore'
    fileContents=fileHandle.readlines()
    for message in fileContents:
      trainingFIle.write(message[0:len(message)-1]+" ")
    trainingFIle.write("\n")

trainingFIle.close()