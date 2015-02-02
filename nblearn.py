__author__ = 'raj'

import sys
dictionaryOfCounts={}
vocabulary={}
classes=[]
vocabularySize=0
training=sys.argv[1]                                    #FROM COMMAND LINE
model=sys.argv[2]                                       #FROM COMMAND LINE

trainingFile=open(training,"r",errors='ignore')                        #errors='ignore'
modelNb=open(model,"w+")

for line in trainingFile.readlines():
    words=line.split()
    message=words[1:]
    label=words[0]

    if label not in classes:
        classes.append(label)

    capLabel=label.capitalize()

    for word in message:
        if word in vocabulary:
            vocabulary[word]+=1
        else:
            vocabulary[word]=1
            vocabularySize+=1
        if label+word in dictionaryOfCounts:
            dictionaryOfCounts[label+word]+=1
        else:
            dictionaryOfCounts[label+word]=1


    if "total"+capLabel in dictionaryOfCounts:
        dictionaryOfCounts["total"+capLabel]+=1
    else:
        dictionaryOfCounts["total"+capLabel]=1

    if "total"+capLabel+"Words" in dictionaryOfCounts:
        dictionaryOfCounts["total"+capLabel+"Words"]+=len(message)
    else:
        dictionaryOfCounts["total"+capLabel+"Words"]=len(message)

    if "totalmessages" in dictionaryOfCounts:
        dictionaryOfCounts["totalmessages"]+=1
    else:
        dictionaryOfCounts["totalmessages"]=1

for typeOfFile in classes:
    modelNb.write("CLASS = "+typeOfFile+"\n")
    dictionaryOfCounts["prior"+typeOfFile.capitalize()+"Probability"]=dictionaryOfCounts["total"+typeOfFile.capitalize()]/dictionaryOfCounts["totalmessages"]

modelNb.write("vocabularySize = "+str(vocabularySize)+"\n")


for key in dictionaryOfCounts.keys():
    modelNb.write(key+" = "+str(dictionaryOfCounts[key])+"\n")

trainingFile.close()
modelNb.close()