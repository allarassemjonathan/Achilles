import os

def setDataSet(languages, final, paths):
    for i in range(len(languages)):
        paths.append(final.strip() + languages[i] + "_bigrams.txt")
    

def LoadDataSet(stringLoc, dico,total):
    f = open(stringLoc, encoding = "utf-8")
    for line in f.readlines():
        dico[line[0:2]] = int(line[3:])
        total += int(line[3:])
    totalL.append(total)

 
def bigramLayer(sentence,dico,guess,totalL):
    for n in range(len(dicolist)):
        if dico == dicolist[n]:
            index = n
            break 
    guess = 0
    sentence = sentence.upper()
    words = sentence.split()
    i = 0
    biagramLayer1 = []
    biagramLayer2 = []
    for word in words:
        if len(word) > 2:
            while i < len(word):
                biagramLayer1.append(word[0 + i: 2 + i])
                i = i + 1
        elif len(word) == 2:
            biagramLayer1.append(word)
    for word in biagramLayer1:
        if len(word)== 2:
            biagramLayer2.append(word)
    for word in biagramLayer2:
        if word in dico.keys():
            guess += float(dico[word]/totalL[index])
        else :
            guess += 0
        
    guesslist.append(guess)

def guessLanguageLayer2(dicolist,paths, sentence, result, languages):
    guess = 0
    for i in range(len(paths)):
        total = 0
        LoadDataSet(paths[i],dicolist[i], total)
        bigramLayer(sentence,dicolist[i],guess,totalL)
    maxi = 0
    index = 0
    for i in range(len(guesslist)):
        if guesslist[i] > maxi:
            maxi = guesslist[i]
            index = i
    result = languages[index]
    print(guesslist)
    print(maxi)
    print(result)

    
def learning(result,truth ,sentence,dicolist,paths, languages):
    guessLanguageLayer2(dicolist, paths, sentence, result, languages)
    if result != truth:
        arr = sentence.split()
        f = open(truth + '_learning.txt', 'a')
        for i in arr:
            f.write(i)
            f.write(' ')
    f.close()

    
totalL = []
languages = ['german','french','spanish','english']
final = r'''C:\Users\ALLARASSEMJJ20\Downloads\
'''
paths = []
total = 0
setDataSet(languages, final,paths)
dicoF = {}
dicoE = {}
dicoG = {}
dicoS = {}
dicolist = [dicoG,dicoF,dicoS,dicoE]
guesslist = []
sentence = input("enter a sentence ")
result = ''
guessLanguageLayer2(dicolist,paths,sentence, result, languages)
truth = 'french'
result = ''
#learning(result, truth, sentence, dicolist, paths, languages)
#guessLanguageLayer1(sentence,languages,guesslist)



