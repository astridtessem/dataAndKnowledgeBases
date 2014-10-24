import math
from readData import *
import random as r

#___________________________________________________________
#Viterbi algorithm(hmm)
def viterbi(obs, states, start_p, trans_p, emit_p):
    #This will keep track over the probability of each state for every observation
    V = [{}]
    
    #Level 0 of the algorithm(special case)
    for i in states:
        V[0][i] = start_p[i]*emit_p[i][obs[0]]
    #Iterate the rest of the observations and adding them to V
    for i in range(1,len(obs)):
        V.append({})

        
        for j in states:
            maxValue = []
            if(obs[i] not in emit_p[j]):
                #If the word is not in the corpus - Have to find something out!
                #Now it only assings the same values as the last observation(step)
                V[i][j] = V[i-1][j]
            else:
                emit = emit_p[j][obs[i]]
                for k in range(0,len(states)):
                    maxValue.append(V[i-1][states[k]]*trans_p[states[k]][j])
                V[i][j] = emit*max(maxValue)

    return V
