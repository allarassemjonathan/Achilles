def write(dico, language):
    f = open(language + "blabla_bigrams.txt","w",encoding = "utf-8")
    for key in dico.keys():
        f.write(key + ' ' + str(dico.get(key)) + '\n')
    f.close()


def setDataSet(languages, final, paths):
    for i in range(len(languages)):
        paths.append(final.strip() + languages[i] + "_bigrams.txt")
    

def LoadDataSet(stringLoc, dico,total):
    f = open(stringLoc, encoding = "utf-8")
    for line in f.readlines():
        dico[line[0:2]] = int(line[3:])
        total += int(line[3:])
    totalL.append(total)



def bigramLayer(sentence,dico,guess,totalL, index):
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
    for word in biagramLayer1:
        if len(word)== 2:
            biagramLayer2.append(word)
    for word in biagramLayer2:
        if word in dico.keys():
            guess += float(dico[word]/totalL[index])
        else :
            guess += 0
    guesslist.append(guess)


def guessLanguageLayer2(dicolist,paths, sentence, result, languages, index):
    guess = 0
    for i in range(len(paths)):
        total = 0
        LoadDataSet(paths[i],dicolist[i], total)
        bigramLayer(sentence,dicolist[i],guess,totalL, index)
    maxi = 0
    for i in range(len(guesslist)):
        if guesslist[i] > maxi:
            maxi = guesslist[i]
            index = i
    result = languages[index]
    print(guesslist)
    print(maxi)
    print(result)
    

def learning(result,truth ,sentence,dicolist,paths, languages):
    index = 0
    guessLanguageLayer2(dicolist, paths, sentence, result, languages, index)
    print(dicolist[index])
    if result != truth:
        words = sentence.upper().split()
        i = 0
        Layer1 = []
        Layer2 = []
        for word in words:
            if len(word) > 2:
                while i < len(word):
                    Layer1.append(word[0 + i: 2 + i])
                    i = i + 1
            elif len(word) ==2:
                Layer1.append(word)
        for word in Layer1:
            if len(word)== 2:
                Layer2.append(word)
        for n in range(len(languages)):
            print(truth + ' ' + languages[n])
            print(n)
            if language[n] == truth:
                break
        dico = dicolist[n]
        for key in Layer2:
            if key in dico.keys():
                dico[key] = dico.get(key) + 1
            else :
                dico[key] = 1
        write(dico, truth)
    print(dico)


def apprendre(language,dicolist, languages, book):
    f = open(book, 'r',  encoding = "utf-8")
    for sentence in f.readlines():
        words = sentence.upper().split()
        i = 0
        Layer1 = []
        Layer2 = []
        for word in words:
            if len(word) > 2:
                while i < len(word):
                    Layer1.append(word[0 + i: 2 + i])
                    i = i + 1
            elif len(word) ==2:
                Layer1.append(word)
        for word in Layer1:
            if len(word)== 2:
                Layer2.append(word)
        for n in range(len(languages)):
            if language[n] == truth:
                break
        dico = dicolist[n]
        for key in Layer2:
            if key in dico.keys():
                dico[key] = dico.get(key) + 1
            else :
                dico[key] = 1
    write(dico, language)
        
    






    
result = ''
truth = 'english'
#sentence = input('give a value ')
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
index = 0
language = 'french'
book = 'sentences.txt'
#learning(result, truth,sentence,dicolist,paths,languages)
apprendre(language,dicolist,languages, book)










