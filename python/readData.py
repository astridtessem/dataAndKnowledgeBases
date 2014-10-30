from os import path
import os
import random

def readDataFile(fileName):    
    with open(fileName) as f:
        content = f.readlines()
    corp = []
    for i in range(0,len(content)):
        b = content[i].split()
        corp.append((b[0],b[1]))
    return corp;


def getObs(text):
    return tuple(text.split(' '))


def readCorpus(number):
    
    content = [];
    #Creates a list of all documents in dir and load them to memory"
    fileList = os.listdir(path.relpath("Corpus"));
    
    for i in range(0,number):
        #Get random document
        r = random.randrange(0,len(fileList))
        
        with open(path.relpath("Corpus/"+fileList[r])) as f:
                content = content + f.read().splitlines()
    
    corp = []
    for i in range(0,len(content)):
        b = content[i].split();
        if(len(b)==7):
            #print(b[6])
            if(b[6]=="B-Org" or b[6]=="I-Org" or b[6]=="I-OrgTeam" or b[6]=="B-OrgTeam" or b[6]=="I-OrgTeam"):
                corp.append((b[2],"OR"));    
            elif(b[6]=="B-Peop" or b[6]=="I-Peop" ):
                corp.append((b[2],"P"));
            elif(b[6]=="B-Num" or b[6]=="I-Num" or b[6] =="B-Money"):
                corp.append((b[2],"N"));
            elif(b[6]=="B-Date" or b[6]=="I-Date"):
                corp.append((b[2],"D"));
            elif(b[6]=="B-Loc" or b[6]=="B-LocCit" or b[6]=="B-LocStat" or b[6]=="I-LocCit"):
                corp.append((b[2],"L"));
            else:
                corp.append((b[2],"O"));
    return corp



