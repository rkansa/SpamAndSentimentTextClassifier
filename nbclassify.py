__author__ = 'raj'

import glob
import os
import sys
from math import log

modelDictionary={}
classes=[]
#directory= "/home/raj/repos/SPAM_dev/*.txt"
#directory= "/home/raj/repos/csci544-hw0/data/*.txt"
#modelFile=open("sentiment.nb","r")
          #FROM COMMAND LINE
                                    #FROM COMMAND LINE
model=sys.argv[1]
directory=sys.argv[2]
print(directory)
print(model)
#model="spam.nb"
if model=="spam.nb":
    out="spam.out"
elif model=="sentiment.nb":
    out="sentiment.nb"
output=open(out,"w")
modelFile=open(model,"r",errors='ignore')                       #errors='ignore'
for line in modelFile.readlines():
    word=line.split()
    if word[0]=="CLASS":
        classes.append(word[2])
        continue
    modelDictionary[word[0]]=word[2]
modelFile.close()


def calculateProbOfWordGivenClass(word,fileType):
    if fileType+word in modelDictionary:
        count=modelDictionary[fileType+word]
        numAddone=int(count)
        numAddone+=1
    else:
        numAddone=1

    totalfileTypeWords=int(modelDictionary["total"+fileType.capitalize()+"Words"])
    vocabularySize=int(modelDictionary["vocabularySize"])
    denomAfterAddone=totalfileTypeWords+vocabularySize
    return float(numAddone/denomAfterAddone)

testFile=open("test.txt","w+")

inputDir=glob.glob(directory)
for file in inputDir:
    fileName= os.path.split(file)[1]                #Need to remove
    label=fileName.split(".")[0]                    #These three lines
    testFile.write(label+" ")                       #After COmputing Accuracy
    fileHandle=open(file,"r",errors='ignore')                       #errors='ignore'
    fileContents=fileHandle.readlines()
    for message in fileContents:
      testFile.write(message[0:len(message)-1]+" ")
    testFile.write("\n")
testFile.close()

testFile=open("test.txt","r",errors='ignore')                       #errors='ignore'

for line in testFile.readlines():
    higherprobability=-9999999999999999
    label=""
    words=line.split()
    for fileType in classes:
        for word in words:
            modelDictionary["prob"+word+"Given"+fileType.capitalize()+"Class"]=calculateProbOfWordGivenClass(word,fileType)
            if "probDocumentGiven"+fileType.capitalize()+"Class" in modelDictionary:

                modelDictionary["probDocumentGiven"+fileType.capitalize()+"Class"]+=log(modelDictionary["prob"+word+"Given"+fileType.capitalize()+"Class"])
            else:
                modelDictionary["probDocumentGiven"+fileType.capitalize()+"Class"]=log(modelDictionary["prob"+word+"Given"+fileType.capitalize()+"Class"])
        modelDictionary["prob"+fileType.capitalize()+"GivenDocument"]=log(float(modelDictionary["prior"+fileType.capitalize()+"Probability"]))+float(modelDictionary["probDocumentGiven"+fileType.capitalize()+"Class"])
        if modelDictionary["prob"+fileType.capitalize()+"GivenDocument"]>higherprobability:
            higherprobability=modelDictionary["prob"+fileType.capitalize()+"GivenDocument"]
            label=fileType
        modelDictionary["prob"+fileType.capitalize()+"GivenDocument"]=0
        modelDictionary["probDocumentGiven"+fileType.capitalize()+"Class"]=0
    output.write(label+"\n")







