import sys
import json
from ViterbiAlgorithm import *
from featureExtraction import *


#Read the json files - input name of file
def readJson(name):
    with open(path.relpath("ViterbiData/" + name +'.json')) as f:
        data = json.load(f)
    return data


def readData(i):
    trans_p = readJson("trans_p"+str(i))
    emit_p = readJson("emit_p"+str(i))
    states = readJson("states"+str(i))
    start_p = readJson("start_p"+str(i))
    return trans_p,emit_p,states,start_p

#Takes in the text and the number of different models to iterate over. 
def main(text,numOfMod):
    print("Running Viterbi on " + str(numOfMod) + " different models:");    
    #Splitting the input observations into tuple e.g ('Joe', 'is', 'a', 'person')
    text = text.replace(".","") #Removing .
    text = text.replace(",","")
    text = text.replace(":","")

    obs = tuple(text.split(' '))

    bigV = []

    #Run the viterbi algorithm over the different models and save the result in finV
    for i in range(numOfMod):
        trans_p,emit_p,states,start_p = readData(i)
        #Run the viterbi algorithm
        V = viterbi(obs,states,start_p,trans_p,emit_p);
        result = []
        for j in range(0,len(V)):
            result.append(max(V[j],key=V[j].get))
        bigV.append(result);
        print("Iteration" + str(i) + " is completed.")

    mlp = []
    
    #Based on the different models, find the most likely path
    for i in range(len(obs)):
        temp = [];
        for j in range(numOfMod):
            temp.append(bigV[j][i])
        mlp.append(temp);

    result = []
    for i in range(len(obs)):
        result.append(max(set(mlp[i]),key=mlp[i].count))
    print("Viterbi result:")
    for i in range(len(result)):
        print(obs[i],result[i])
    return result;

main("This is a test. Five is a number",3)

