from backend.ModulLanguage import LowerCase

def BMSearch(sentence, keyword):
    sentence = LowerCase(sentence)
    keyword = LowerCase(keyword)
    sLength = len(sentence)
    wLength = len(keyword)

    dictLastChar = GetDictOfChar(keyword)

    result = False
    i = wLength-1 #idx sentence
    j = wLength-1 #idx keyword
    while i<sLength and not(j==0 and i>sLength-wLength):
        if sentence[i]==keyword[j] :
            if j==0 :
                result = True
                break
            i-=1
            j-=1
        elif sentence[i] in dictLastChar.keys() :
            if j > dictLastChar.get(sentence[i]) :
                i = i+wLength-1-dictLastChar.get(sentence[i])
                j = wLength-1
            else:
                i = i+wLength-j 
                j = wLength-1
        else:
            i = i+wLength
            j = wLength-1
    findAt = i #location keyword find in sentence
    return result

def GetDictOfChar(string):
    result = {}
    for i in range(len(string)):
        result[string[i]] = i
    return result