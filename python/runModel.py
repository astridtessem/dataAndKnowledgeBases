import sys
import json
from ViterbiAlgorithm import *

#Load the different matrixes into memory
def readData():
    trans_p = readJson("trans_p")
    emit_p = readJson("emit_p")
    states = readJson("states")
    start_p = readJson("start_p")
    return trans_p,emit_p,states,start_p

#Read the json files - input name of file
def readJson(name):
    with open(path.relpath("ViterbiData/" + name +'.json')) as f:
        data = json.load(f)
    return data


def main(text):
    trans_p,emit_p,states,start_p = readData()
    #Splitting the input observations into tuple e.g ('Joe', 'is', 'a', 'person')
    text = text.replace(".","") #Removing .
    obs = tuple(text.split(' '))
    #Run the viterbi algorithm
    V = viterbi(obs,states,start_p,trans_p,emit_p);
    #Print out the result
    s = ""
    for i in range(0,len(V)):
        #s +=max(V[i],key=V[i].get)+" "
        print(obs[i],max(V[i],key=V[i].get))
    #print(s)

#To run the method from Meteor
    
##if __name__ == "__main__":
##    size = len(sys.argv)
##    a = "";
##    for i in range(2,size):
##        a += str(sys.argv[i]) + " "
##    a = a.rstrip()
##    main(a)

       
main("Joe is playing fotball in San Fransico in November. Bob have never played it before")
    


