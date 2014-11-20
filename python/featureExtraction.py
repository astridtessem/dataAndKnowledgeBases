from features import *

def featureExtraction(result,obs):
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
                
    return result


def featureEmitFail(word,state):
    if(state=="D" and isDate(word)):
        return True;
    if(state=="D" and isMonth(word)):
        return True;
    if(state=="N" and isPhoneNumber(word)):
        return True;
    if(state=="L" and isCity(word)):
        return True;
    if(state=="L" and isCountry(word)):
        return True;
    if(state=="P" and isPerson(word)):
        return True;

    return False
