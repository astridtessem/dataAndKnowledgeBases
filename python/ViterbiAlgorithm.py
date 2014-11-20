import math
from readData import *
import random as r
from featureExtraction import *

#___________________________________________________________
#Viterbi algorithm(hmm)
def viterbi(obs, states, start_p, trans_p, emit_p):
    #This will keep track over the probability of each state for every observation
    V = [{}]
    
    #Level 0 of the algorithm(special case)
    for i in states:
        #If the word is not in the emit matrix. Use feature extraction and try to classify it
        #and give it a value. If the feature do not find it, give it a low 
        if(obs[0] not in emit_p[i]):
            #Input word and state
            if(featureEmitFail(obs[0],i)):
                V[0][i] = start_p[i]*0.00015;
            else:
                V[0][i] = start_p[i]*0.000000002;

        #Normal behaviour
        else:
            V[0][i] = start_p[i]*emit_p[i][obs[0]]
            
    #Iterate the rest of the observations and adding them to V
    for i in range(1,len(obs)):
        V.append({})
        
        for j in states:
            maxValue = []

            #if word not in emit. Set a emit value based on feature extraction
            if(obs[i] not in emit_p[j]):
                if(featureEmitFail(obs[i],j)):
                    emit = 0.00015
                else:
                    emit = 0.000000002
            else:
                emit = emit_p[j][obs[i]]


            for k in range(0,len(states)):
                maxValue.append(V[i-1][states[k]]*trans_p[states[k]][j])
            V[i][j] = emit*max(maxValue)

    return V
