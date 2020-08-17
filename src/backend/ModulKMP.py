from backend.ModulLanguage import LowerCase

def KMPSearch(sentence, keyword):
    sentence = LowerCase(sentence)
    keyword = LowerCase(keyword)
    sLength = len(sentence)
    wLength = len(keyword)

    result = False
    i = 0 #idx sentence
    j = 0 #idx keyword
    while i<sLength and not(j==0 and i>sLength-wLength): 
        if keyword[j]==sentence[i] : 
            if j==wLength-1 :
                result = True
                break
            i += 1
            j += 1
        elif j>0:
            j=BorderFuntion(keyword, j)
        else:
            i += 1
    findAt = i + 1 - wLength #location keyword find in sentence
    return result

def BorderFuntion(keyword, j):
    if j==1 :
        return 0
    else :
        prefix = keyword[:j]
        suffix = keyword[1:j]
        temp = len(suffix)
        while temp>0:
            if prefix[:temp]==suffix[len(suffix)-temp:] :
                break
            else:
                temp-=1
        return temp