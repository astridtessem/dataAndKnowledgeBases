import math
import numpy
from readData import *

#corp = [("Hans-Olav","P"),("en","O"),("en","O"),("elev","O"),("på","O"),("UCSB","OR")]
#corp = [("UCSB","OR"),("er","O"),("en","O"),("elev","O"),("på","O"),("Hans-Olav","P")]
#print(corp)

states = ("P","O","OR","N","D")
#print("States:",states)

corp = readCorpus('1.txt')
def getStateProp(states,corpus):
    p = 0;
    o = 0;
    org = 0;
    d = 0;
    n = 0;
    for item in corpus:
        if(item[1]=="P"):
            p+=1
        elif(item[1]=="O"):
            o+=1
        elif(item[1]=="D"):
            d+=1
        elif(item[1]=="N"):
            n+=1
        else:
            org+=1
    c = len(corpus)
    return {'P':p/c,'O':o/c,'OR':org/c,'D':d/c,'N':n/c}
    
start_p = getStateProp(states,corp);
print(start_p,"StartProb")
print("");

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

def getTransitionProp(state,corpus):
    trans_p = {}
    #Create dictionary
    for i in range(0,len(state)):
        temp = {}
        for j in range(0,len(state)):
            temp[state[j]] = 0
        trans_p[state[i]] = temp

    #Count word occurens in pattern( e.g "Hans"(P) to "er"(O))
    for i in range(0,len(state)):
        for j in range(0,len(states)):
            for k in range(0,len(corpus)-1):
                if(corpus[k][1]==state[i] and corpus[k+1][1]==state[j]):
                    trans_p[state[i]][state[j]] +=1
                    
    #Convert to just entities - easier to count.
    corpusEntity = converToEntity(corpus)
    for i in range(0,len(state)):
        for j in range(0,len(states)):
            #Divides the occurence by the number of entity-type in corpus
            trans_p[state[i]][state[j]]= trans_p[state[i]][state[j]]/corpusEntity.count(state[i])
    return trans_p

def getEmissionProp(states,corpus):
    #Convert the corpus to tuples, easier to count.. TODO
    corpusEntity = converToEntity(corpus)
    #Conver the corpus to words, easier to count...TODO
    corpusWords = converToWord(corpus);

    emit_p = {}
    
    for i in range(0,len(states)):
        temp = {}
        for j in range(0,len(corpus)):
            if(corpus[j][1]==states[i]):
                countEntity = corpusEntity.count(states[i])
                temp[corpus[j][0]] = corpusWords.count(corpus[j][0])/countEntity
            else:
                temp[corpus[j][0]] = 0;
        emit_p[states[i]] = temp
    return emit_p

def printDic(dic):
    for i in dic:
        print(i)
        for j in dic[i]:
            print(j,":",dic[i][j])
    
trans_p = getTransitionProp(states,corp)
emit_p = getEmissionProp(states,corp)
print("_______Transmission______")
#printDic(trans_p);

print("_______Emission__________")
#printDic(emit_p);

print("_______Start_P______")
print(start_p)

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    
    #Setting the first. 
    for i in states:
        V[0][i] = start_p[i]*emit_p[i][obs[0]]
    #The next
    for i in range(1,len(obs)):
        V.append({})
        
        for j in states:
            maxValue = []
            if(obs[i] not in emit_p[j]):
                V[i][j] = 0.1
                print(obs[i])
            else:
                emit = emit_p[j][obs[i]]
                
                for k in range(0,len(states)):
                    maxValue.append(V[i-1][states[k]]*trans_p[states[k]][j])
                V[i][j] = emit*max(maxValue)  
    return V

def getRandomSentence(corp,l):
    sentence = ""
    for i in range(0,l):
        

print("Viterbi alg is starting")
obs = getRandomSentence(corp,10);
obs = getObs("the people here are never")
V = viterbi(obs,states,start_p,trans_p,emit_p);
for i in V:
    print(i)
for i in range(0,len(V)):
    print(obs[i],max(V[i],key=V[i].get))
    
