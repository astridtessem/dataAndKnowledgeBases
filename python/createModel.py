import math
from readData import *
import random as r
from ViterbiModel import *
import json
import time


def jsonSave(data,name):
    with open(path.relpath('ViterbiData/'+name+'.json'), 'w') as fp:
        json.dump(data, fp)
    


def saveModel(trans_p,emit_p,states,start_p):
    jsonSave(trans_p,"trans_p")
    jsonSave(emit_p,"emit_p")
    jsonSave(states,"states")
    jsonSave(start_p,"start_p")


def createModel():
    tic = time.clock()

    #Read corpus - inpurt: number of documents
    corp = readCorpus(50);
    

    #The different states
    states = getStates(corp)
    print("States completed")
    
    #Creates the start probability
    start_p = getStateProp(states,corp);
    print("Start completed")

    #Get the transmition and the emition matrix
    trans_p = getTransitionProp(states,corp)
    print("Trans completed")
    emit_p = getEmissionProp(states,corp)
    print("Emit completed")

    toc = time.clock()
    print("Time: ",toc-tic)

    saveModel(trans_p,emit_p,states,start_p)

createModel()
