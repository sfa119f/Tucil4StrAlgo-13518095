'''
number of algorithm:
    1 : Booyer-Moore(BM)
    2 : Knuth-Morris-Pratt(KMP)
    3 : Regex
'''
from flask import Flask, render_template, request, flash, redirect, url_for
from frontend import app
from frontend.form.Interface import InterfaceForm
from frontend.form.Result import ResultPage
from frontend.form.About import AboutPage
from backend.ModulFile import GetListFile, GetFileName
from backend.ExtracInfo import Extrac

@app.route('/', methods=['GET', 'POST'])
def Interface():
    interfaceForm = InterfaceForm()
    if interfaceForm.validate_on_submit():
        if not interfaceForm.algorithm.errors:
            listFile = GetListFile(interfaceForm.folder.data)
            if len(listFile) == 0:
                flash('Warning!!!')
                flash('File .txt Not Found  or Incorrect Directory')
            else:
                listResult = Extrac(listFile, interfaceForm.algorithm.data, interfaceForm.keyword.data)
                #print(listFile)
                #print(interfaceForm.algorithm.data)
                #print(interfaceForm.keyword.data)
                #print(listResult)
                #listResult = [1,2,3,4,5,6,7,8,9,10]
                if len(listResult) == 0:
                    flash('Sorry :(')
                    flash('Keyword Not Found in All File')
                else:
                    if interfaceForm.algorithm.data==1 :
                        alg = 'Booyer-Moore (BM)'
                    elif interfaceForm.algorithm.data==2 :
                        alg = 'Knuth-Morris-Pratt (KMP)'
                    else :
                        alg = 'Regex'
                    RListFilename = []
                    RListTotal = []
                    RListTime = []
                    RListSentence = []
                    for res in listResult:
                        RListFilename.append(GetFileName(res[0]))
                        RListTotal.append(res[1])
                        RListTime.append(res[2])
                        RListSentence.append(res[3])
                    return redirect(url_for('Result', keyword=interfaceForm.keyword.data, algorithm=alg, listFilename=RListFilename, listTotal=RListTotal, listTime=RListTime, listSentence=RListSentence, totalFind=len(listResult)))
    return render_template('Interface.html', title='SFA InfoExtraction App', form=interfaceForm)

@app.route('/Result')
def Result():
    keyword = request.args.get('keyword')
    algorithm = request.args.get('algorithm')
    RListFilename = request.args.getlist('listFilename')
    RListTotal = request.args.getlist('listTotal')
    RListTime = request.args.getlist('listTime')
    RListSentence = request.args.getlist('listSentence')
    totalFind = int(request.args.get('totalFind'))
    listResult = []
    for i in range(totalFind):
        temp = (RListFilename[i], RListTotal[i], RListTime[i], RListSentence[i])
        listResult.append(temp)
    resultPage = ResultPage(keyword, algorithm, totalFind, listResult)
    return render_template('Result.html', title="Result Extraction", page=resultPage)

@app.route('/About')
def About():
    aboutPage = AboutPage()
    return render_template('About.html', title='About App', page=aboutPage)