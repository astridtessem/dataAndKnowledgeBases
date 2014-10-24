import re


def isDate(text):
    mat=re.match('([0-2][0-9]|[3][0-1])[/.-]([0][0-9]|[1][0-2])[/.-]([0-2]\d{3})$',text)
    if(mat is None):
        return False;
    return True;


def isPhoneNumber(text):
    mat=re.match('\(?\d{3}\)?\s?\d{3}(\-?|\s?)\d{4}',text)
    if(mat is None):
        return False;
    return True;

def isMonth(text):
    month = ["january","february","march","april","may","june","july","august","september","october","november","december"]
    if text.lower() in month:
        return True
    return False

print(isDate("10.12.2014"))
print(isPhoneNumber('(805) 280-6071'))
print(isMonth("January"))


