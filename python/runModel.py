import sys
import json
from ViterbiAlgorithm import *
from features import *

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
    # NEED TO REMOVE MORE THAN COMMA, WHAT ABOUT : 
    obs = tuple(text.split(' '))
    
    #Run the viterbi algorithm
    V = viterbi(obs,states,start_p,trans_p,emit_p);
    
    #Print out the result
    result = []
    for i in range(0,len(V)):
        result.append([obs[i],max(V[i],key=V[i].get)])
        #print(obs[i],max(V[i],key=V[i].get))
    print(result)
    
    #Check features - just checking if it works
    print("____________Feature extraction_________")
    for i in range(0,len(result)):
        #Check only if it is classified as other.. Classified wrong without it...
        if(result[i][1] =="O"):
            if(isCity(result[i][0])):
                result[i][1] = "L"
            if(isCountry(result[i][0])):
                result[i][1] = "L"
            if(isPerson(result[i][0])):
                result[i][1] = "P"
            if(isMonth(result[i][0])):
                result[i][1] = "D"
            if(isDate(result[i][0])):
                result[i][1] = "D"
            if(isPhoneNumber(result[i][0])):
                result[i][1] = "N"
    print(result)

def new_readData(i):
    trans_p = readJson("trans_p"+str(i))
    emit_p = readJson("emit_p"+str(i))
    states = readJson("states"+str(i))
    start_p = readJson("start_p"+str(i))
    return trans_p,emit_p,states,start_p

#Takes in the text and the number of different models to iterate over. 
def new_main(text,numOfMod):
    print("Running Viterbi on " + str(numOfMod) + " different models:");
    #Splitting the input observations into tuple e.g ('Joe', 'is', 'a', 'person')
    text = text.replace(".","") #Removing .
    # NEED TO REMOVE MORE THAN COMMA, WHAT ABOUT : 
    obs = tuple(text.split(' '))

    bigV = []

    #Run the viterbi algorithm over the different models and save the result in finV
    for i in range(numOfMod):
        trans_p,emit_p,states,start_p = new_readData(i)
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

    result = [];
    for i in range(len(obs)):
        result.append(max(set(mlp[i]),key=mlp[i].count))
        
    print("Viterbi result:",result)
    
    print("Running feature extraction:")
    for i in range(0,len(result)):
        #Check only if it is classified as other.. Classified wrong without it...	
        if(result[i] =="O"):
            if(isCity(obs[i])):
                result[i] = "L"
            if(isCountry(obs[i])):
                result[i] = "L"
            if(isPerson(obs[i])):
                result[i] = "P"
            if(isMonth(obs[i])):
                result[i] = "D"
            if(isDate(obs[i])):
                result[i] = "D"
            if(isPhoneNumber(obs[i])):
                result[i] = "N"
    print("Feature extraction after Viterbi:",result)
    

#To run the method from Meteor
    
##if __name__ == "__main__":
##    size = len(sys.argv)
##    a = "";
##    for i in range(2,size):
##        a += str(sys.argv[i]) + " "
##    a = a.rstrip()
    ##    main(a)

    
new_main("am playing fotball in London in November",3)
    


