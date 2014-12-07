from runModel import new_main
from readData import *
import random


def wash(corp):
    washWords = ["'","`",",",".",":","''","COMMA",'"',"_","``","`","-"]
    washedCorp = [];
    for i in range(len(corp)):
        if(corp[i][0] not in washWords):
            washedCorp.append(corp[i])
            
    return washedCorp

def createSentences(corp):
    sentences = []
    entities = [];
    sentence = "";
    for i in range(len(corp)):
        if(corp[i]=="NEW"):
            sentences.append((sentence,entities));
            sentence = ""
            entities = []
        else:
            sentence +=corp[i][0] + " "
            entities.append(corp[i][1])
        
    return sentences

def test(numberOfWords,numberOfDocuments,numberOfModels):

    
    i = 0
    correct = 0
    while(i<numberOfWords):
        corp = readTestDocument()
        corp = wash(corp);
        sentences = createSentences(corp)
        if(len(sentences)>0):
            r = random.randrange(0,len(sentences))
            
            vResult = new_main(sentences[r][0],numberOfModels);
            for j in range(0,len(vResult)-1):
                if(vResult[j]==sentences[r][1][j]):
                    correct +=1
                    
                i+=1;
    print("Words: " + str(i),"Correct: "+ str(correct))
    print(correct/i)
    return correct/i;
        
        

numTest = 30
numWord = 200

total = 0; 
for i in range(0,numTest):
    total +=test(numWord,1,3)

print("Based on " + str(numTest) + "tests with "+ str(numWord)+ "s the accuarcy is : " +str(total/numTest));




