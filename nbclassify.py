__author__ = 'raj'

import sys
from math import log
modelDictionary={}
classes=[]
model=sys.argv[1]
if model=="spam.nb":
    out="spam.out"
elif model=="sentiment.nb":
    out="sentiment.out"
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
test=sys.argv[2]
testFile=open(test,"r",errors='ignore')                       #errors='ignore'

for line in testFile.readlines():
    higherprobability=-float("inf")
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
    print(label)







