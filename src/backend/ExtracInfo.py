'''
number of algorithm:
    1 : Booyer-Moore(BM)
    2 : Knuth-Morris-Pratt(KMP)
    3 : Regex
'''
from backend.ModulFile import GetFileContents
from backend.ModulLanguage import SplitSentence
from backend.ModulBM import BMSearch
from backend.ModulKMP import KMPSearch
from backend.ModulReg import RegexSearch, GetDate, GetTotal

def Extrac(listFile, algorithm, keyword):
    result = []
    for file in listFile:
        temp = False
        contentFile = GetFileContents(file)
        for paragraph in contentFile:
            sentence = SplitSentence(paragraph)
            for s in sentence:
                articleDate = GetDate(s)
                if articleDate :
                    temp = True
            if temp :
                break
        for paragraph in contentFile:
            sentence = SplitSentence(paragraph)
            for s in sentence:
                if(algorithm==1):
                    isAvailable = BMSearch(s, keyword)
                elif(algorithm==2):
                    isAvailable = KMPSearch(s, keyword)
                elif(algorithm==3):
                    isAvailable = RegexSearch(s, keyword)
                if isAvailable :
                    total = GetTotal(s, keyword)
                    if total :
                        #print(total)
                        date = GetDate(s)
                        if date :
                            tuples = (file, total, date, s)
                        else :
                            tuples = (file, total, articleDate, s)
                        result.append(tuples)
    return result