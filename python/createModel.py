import math
from readData import *
import random as r
from ViterbiModel import *
import json
import time


def jsonSave(data,name):
    with open(path.relpath('ViterbiData/'+name+'.json'), 'w') as fp:
        json.dump(data, fp)
    


def saveModel(trans_p,emit_p,states,start_p,modelNumber):
    
    jsonSave(trans_p,"trans_p"+str(modelNumber))
    jsonSave(emit_p,"emit_p"+str(modelNumber))
    jsonSave(states,"states"+str(modelNumber))
    jsonSave(start_p,"start_p"+str(modelNumber))


def createModel(numberOfModels, numberOfDocuments):

    for i in range(0,numberOfModels):
        tic=time.clock()

        #Read corpus for model number i
        corp = readCorpus(numberOfDocuments)

        #The different states for model number i
        states = getStates(corp)
        print("states completed for model number")

        #Creates the starp probability for model number i
        start_p=getStateProp(states, corp);
        print("start_p completed for model number")

        #Get the transmition and the emition matrix
        trans_p = getTransitionProp(states,corp)
        print("Trans completed for model number")

        emit_p = getEmissionProp(states,corp)
        print("Emit completed for model number")

        toc = time.clock()
        print("Time: ",toc-tic)

        saveModel(trans_p,emit_p,states,start_p,i)

createModel(3,50)
