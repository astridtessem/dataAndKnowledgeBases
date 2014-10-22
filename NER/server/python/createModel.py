import math
import numpy
from readData import *
import random as r
from ViterbiModel import *
import json


def jsonSave(data,name):
    with open(name+'.json', 'w') as fp:
        json.dump(data, fp)
    


def saveModel(trans_p,emit_p,states,start_p):
    jsonSave(trans_p,"trans_p")
    jsonSave(emit_p,"emit_p")
    jsonSave(states,"states")
    jsonSave(start_p,"start_p")


def createModel():
    #Fetch the corpus
    corp = readCorpus('1to20.txt')
    #corp = readCorpus('1.txt')
    #corp = readDataFile('AndreVerdenskrigData.txt');

    #The different states
    states = getStates(corp)
    
    #Creates the start probability
    start_p = getStateProp(states,corp);

    #Get the transmition and the emition matrix
    trans_p = getTransitionProp(states,corp)
    emit_p = getEmissionProp(states,corp)


    saveModel(trans_p,emit_p,states,start_p)

createModel()
