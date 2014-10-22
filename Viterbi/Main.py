import math
import numpy
from readData import *
import random as r
from ViterbiAlgorithm import *
from ViterbiModel import *

#Main-file
#Generates a random sentence from the corpus

def getRandomSentence(corp,l):
    sentence = ""
    for i in range(0,l):
        sentence += corp[r.randint(0,len(corp))][0] + " "
    return sentence;

#___________________________________________________________
#Starting the viterbi algorithm and prints the probability of each word in each state
print("________Viterbi alg is starting________________")

#Gets a random sentence from the corpus
obs = getRandomSentence(corp,20);
#obs = "Første verdenskrig endret radikalt det politiske kartet i Europa"

print(obs)
#Converting to readable format
obs = getObs(obs)
V = viterbi(obs,states,start_p,trans_p,emit_p);
for i in V:
    print(i)
for i in range(0,len(V)):
    print(obs[i],max(V[i],key=V[i].get))
