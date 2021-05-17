import os

''' update the diagram of frequencies(model)
'''
def write(dico, language):
    f = open(language + "blabla_bigrams.txt", "w", encoding = "utf-8")
    for key in dico.keys():
        f.write(key + ' ' + str(dico.get(key)) + '\n')
    f.close()
    print(dico)

''' set the path to load the data
'''
def setDataSet(languages, final, paths):
    for i in range(len(languages)):
        paths.append(final.strip() + languages[i] + "blabla_bigrams.txt")
    
''' load the model from the dataset
'''
def LoadDataSet(stringLoc, dico,total):
    f = open(stringLoc, encoding = "utf-8")
    for line in f.readlines():
        dico[line[0:2]] = int(line[3:])
        total += int(line[3:])
    totalL.append(total)

''' use bigrams to make predictions
'''
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

''' guess the language
'''
def guessLanguageLayer2(dicolist,paths, sentence, result, languages, index):
    print('here')
    guess = 0
    for i in range(len(paths)):
        total = 0
        LoadDataSet(paths[i],dicolist[i], total)
        print(paths[i])
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
    

''' step by step learning to test the apprendre method
'''
def learning(result,dicolist,paths, languages):
    while True:
        index = 0
        sentence = input('Enter a sentence ')
        guessLanguageLayer2(dicolist, paths, sentence, result, languages, index)
        print(dicolist[index])
        truth = input('solution')
        if truth == '-1':
            break
        elif result != truth:
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
            write(dico, truth)

    

''' apprendre method read books and
    improve the diagram of bigrams based on that
'''
def apprendre(language,dicolist, languages, book):
    language = language.capitalize()
    address = final + language + 'Books\\' + book
    address = address.replace('\n', '')
    f = open(address, 'r',  encoding = "ISO-8859-1")
    for sentence in f.readlines():
        punc = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°()-[]{};:'"«»\,+<>./?@#$%^&*_~©'''
        for x in sentence:
            if x in punc:
                sentence = sentence.replace(x,' ')
                
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
            if language[n] == language:
                break
        dico = dicolist[n]
        for key in Layer2:
            if key in dico.keys():
                dico[key] = dico.get(key) + 1
            else :
                dico[key] = 1
    dico = {k:v for k,v in sorted(dico.items(), key = lambda item: item[1])}
    write(dico, language)
        
    
    
result = ''
truth = ''
totalL = []
languages = ['german','french','spanish','english']
final = r'''C:\Users\ALLARASSEMJJ20\Achilles\
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
language = 'german'
string = '''
C:\\Users\\AllarassemJJ20\\Achilles\\
'''
string = string.strip()
books = [os.path.relpath(x) for x in os.listdir(string + language.capitalize() + 'Books\\')]
total = 0
#guessLanguageLayer2(dicolist,paths, sentence, result, languages, index)
#for i in range(len(books)):
#   apprendre(language,dicolist,languages, books[i])

learning(result,dicolist,paths,languages)











