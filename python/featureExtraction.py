from features import *

## This method is run when the word is not in the emission matrix. 
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
