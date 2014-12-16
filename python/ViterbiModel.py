import math
from readData import *
import random as r


#___________________________________________________________
#Converting the corpus to list of entities and words

def converToEntity(corpus):
    l = []
    for word in corpus:
        l.append(word[1]);
    return l;
def converToWord(corpus):
    l = []
    for word in corpus:
        l.append(word[0])
    return l

#___________________________________________________________
#The different states
def getStates(corp):
    entity = converToEntity(corp)
    states = []
    for i in range(0,len(entity)):
        if not entity[i] in states:
            states.append(entity[i])
    return states
#states = getStates(corp)
#print(states)
#states = ("P","O","OR","N","D")

#___________________________________________________________
#Creates the start probability array

def getStateProp(states,corpus):
    p = 0;
    o = 0;
    org = 0;
    d = 0;
    n = 0;
    l = 0;
    
    for item in corpus:
        if(item[1]=="P"):
            p+=1
        elif(item[1]=="O"):
            o+=1
        elif(item[1]=="D"):
            d+=1
        elif(item[1]=="N"):
            n+=1
        elif(item[1]=="L"):
            l+=1;
        elif(item[1]=="OR"):
            org+=1
    c = len(corpus)
    return {'P':p/c,'O':o/c,'OR':org/c,'D':d/c,'N':n/c,'L':l/c}
    

#___________________________________________________________
#Transition matrix

def getTransitionProp(states,corpus):
    trans_p = {}
    #Create dictionary
    for i in range(0,len(states)):
        temp = {}
        for j in range(0,len(states)):
            temp[states[j]] = 0
        trans_p[states[i]] = temp

    #Count word occurens in pattern( e.g "Hans"(P) to "is"(O))
    for i in range(0,len(states)):
        for j in range(0,len(states)):
            for k in range(0,len(corpus)-1):
                if(corpus[k][1]==states[i] and corpus[k+1][1]==states[j]):
                    trans_p[states[i]][states[j]] +=1
                    
    #Convert to just entities - easier to count.
    corpusEntity = converToEntity(corpus)
    for i in range(0,len(states)):
        for j in range(0,len(states)):
            #Divides the occurence by the number of entity-type in corp
            trans_p[states[i]][states[j]]= trans_p[states[i]][states[j]]/corpusEntity.count(states[i])
    return trans_p

#___________________________________________________________
#Emission

def getEmissionProp(states,corpus):
    #Convert the corpus to tuples, easier to count
    corpusEntity = converToEntity(corpus)
    #Conver the corpus to words, easier to count
    corpusWords = converToWord(corpus);

    emit_p = {}
    
    for i in range(0,len(states)):
        temp = {}
        for j in range(0,len(corpus)):
            if(corpus[j][1]==states[i]):
                countEntity = corpusEntity.count(states[i])
                temp[corpus[j][0]] = corpusWords.count(corpus[j][0])/countEntity
            else:
                temp[corpus[j][0]] = 0.000000002;
        emit_p[states[i]] = temp
    return emit_p
#___________________________________________________________
#Print the different dictionaries
def printDic(dic):
    for i in dic:
        print(i)
        for j in dic[i]:
            print(j,":",dic[i][j])


