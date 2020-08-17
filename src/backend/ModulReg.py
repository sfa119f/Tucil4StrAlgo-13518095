import re

def RegexSearch(sentence, keyword):
    temp = re.search(keyword, sentence, flags=re.I)
    if temp :
        findAt = temp.start() #location keyword find in sentence
        return True
    else :
        return False
        
def GetDate(sentence):
    temp = re.search(r'\(?(\d{1,2})([ -.|/])(\w+)([ -./])(\d{2,4})\)?', sentence, flags=re.I)
    if temp :
        date = temp.group()
        day = GetDay(sentence[:temp.start()])
        if day :
            date = day+date
        time = GetTime(sentence[temp.end():])
        print(temp.end())
        if time :
            date = date+time
            print(date)
        return date
    else :
        return None

def GetDay(sentence):
    temp = re.search(r'(senin|selasa|rabu|kamis|(jum\'?at)|sabtu|minggu),? ?', sentence, flags=re.I)
    if (temp and len(sentence) == temp.end()) :
        return temp.group()
    else :
        return None

def GetTime(sentence):
    temp = re.search(r' ((pukul|jam) )?(\d{1,2})([.:]\d{1,2})?([.:]\d{1,2})? ?(wi[bt(ta)]|[pa]m)?', sentence, flags=re.I)
    print(temp)
    if (temp and 0 == temp.start()) :
        return temp.group()
    else :
        return None

def GetTotal(sentence, keyword): #the sentence confirmed has keyword
    temp = re.search(keyword, sentence, flags=re.I)
    start = temp.start()
    end = temp.end()
    temp = re.search(r'(\d{1,3}([,.]\d{3})?)+ ', sentence[:start], flags=re.I)
    prefStart = 0
    prefEnd = 0
    prefix = None
    while temp :
        prefix = temp
        prefStart += temp.start()
        prefEnd += temp.end()
        temp = re.search(r'(\d{1,3}([,.]\d{3})?)+ ', sentence[prefEnd:start], flags=re.I)
    suffix = re.search(r'(\d{1,3}((./,)\d{3})?)+', sentence[end:], flags=re.I)
    if suffix :
        suffStart = suffix.start()+end
        suffEnd = suffix.end()+end
    while prefix and IsCovidStr(sentence, prefStart) :
        stc = sentence[:prefStart]
        tempPre = re.search(r'(\d{1,3}([,.]\d{3})?)+ ', stc, flags=re.I)
        prefStart = 0
        prefEnd = 0
        while tempPre :
            prefix = tempPre
            prefStart += tempPre.start()
            prefEnd += tempPre.end()
            tempPre = re.search(r'(\d{1,3}([,.]\d{3})?)+ ', stc[prefEnd:], flags=re.I)
    while suffix and IsCovidStr(sentence, suffStart) :
        stc = sentence[suffEnd:]
        suffix = re.search(r'(\d{1,3}([,.]\d{3})?)+ ', stc, flags=re.I)
        if suffix :
            suffStart += suffix.start()
            suffEnd += suffix.end()
    if prefix and suffix :
        if start-prefEnd<suffStart-end :
            return prefix.group()
        else :
            return suffix.group()
    elif prefix :
        return prefix.group()
    elif suffix :
        return suffix.group()
    else :
        return None

def IsCovidStr(sentence, pos): #pos is position start substring where is guess 'Covid 19' substring
    temp = re.search(r'covid(\W)?', sentence, flags=re.I)
    if temp :
        if temp.end()==pos :
            return True
        elif temp.end()>pos :
            return False
        else :
            return IsCovidStr(sentence[temp.end():], pos-temp.end())
    else :
        return False
