import os

def GetListFile(path):
    listFile = []
    for root, dirs, file in os.walk(path, topdown=True):
        if root!=path :
            break
        else:
            for f in file:
                if '.txt' in f:
                    listFile.append(os.path.join(root, f))
    return listFile

def GetFileContents(path):
    contents = []
    file = open(path, 'r')
    strLine = file.readline().replace('\n', '').replace('\r', '')
    while strLine != '' :
        contents.append(strLine)
        strLine = file.readline().replace('\n', '').replace('\r', '')
    file.close()
    return contents

def GetFileName(path):
    temp = len(path)
    for i in range(len(path)-1, -1, -1):
        if(path[i] == '\\') :
            temp = i
            break
    return path[temp+1:]