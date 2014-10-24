from os import path

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

def readCorpus(file):
    with open(file) as f:
        content = f.read().splitlines()

    corp = []
    for i in range(0,len(content)):
        b = content[i].split();
        if(len(b)==7):
            #print(b[6])
            if(b[6]=="B-Org" or b[6]=="OrgTeam" or b[6]=="B-OrgTeam"):
                corp.append((b[2],"OR"));    
            elif(b[6]=="B-Peop" or b[6]=="I-Peop"):
                corp.append((b[2],"P"));
            elif(b[6]=="B-Num" or b[6] =="B-Money"):
                corp.append((b[2],"N"));
            elif(b[6]=="B-Date"):
                corp.append((b[2],"D"));
            elif(b[6]=="B-Loc" or b[6]=="B-LocCit" or b[6]=="B-LocStat"):
                corp.append((b[2],"L"));
            else:
                corp.append((b[2],"O"));
    return corp


def readCorpus2():

    #Opens NYT files from NYT_column directory into variable "content"

    for i in range(1,9):
        try:
            with open(path.relpath("Corpus/NYT19980921.000"+str(i))) as f:
                content = f.read().splitlines()
        except:
            pass

    for i in range(10,99):
        try:
            with open(path.relpath("Corpus/NYT19980921.00"+str(i))) as f:
                content = content + f.read().splitlines()
        except:
            pass
        
    for i in range(100,101):
        try:
            with open(path.relpath("Corpus/NYT19980921.0"+str(i))) as f:
                content = content + f.read().splitlines()
        except:
            pass
    
    corp = []
    for i in range(0,len(content)):
        b = content[i].split();
        if(len(b)==7):
            #print(b[6])
            if(b[6]=="B-Org" or b[6]=="OrgTeam" or b[6]=="B-OrgTeam"):
                corp.append((b[2],"OR"));    
            elif(b[6]=="B-Peop" or b[6]=="I-Peop"):
                corp.append((b[2],"P"));
            elif(b[6]=="B-Num" or b[6] =="B-Money"):
                corp.append((b[2],"N"));
            elif(b[6]=="B-Date"):
                corp.append((b[2],"D"));
            elif(b[6]=="B-Loc" or b[6]=="B-LocCit" or b[6]=="B-LocStat" or b[6]=="I-LocCit"):
                corp.append((b[2],"L"));
            else:
                corp.append((b[2],"O"));
    return corp

#corp = readCorpus('1.txt');


