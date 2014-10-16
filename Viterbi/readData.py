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
            if(b[6]==("B-Org" or "OrgTeam")):
                corp.append((b[2],"OR"));    
            elif(b[6]=="B-Peop"):
                corp.append((b[2],"P"));
            elif(b[6]=="B-Num"):
                corp.append((b[2],"N"));
            elif(b[6]=="B-Date"):
                corp.append((b[2],"D"));
            else:
                corp.append((b[2],"O"));
    return corp

#corp = readCorpus('1.txt');



