import nltk

f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\Frankeshtein.txt', encoding = 'utf-8')
li = []
s = f.read()
s = s.lower()
dic ={}
dicW= {}
punc = '.!'
forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789→°‘()-—[]{};:'“”"«»\+<>/@#$%^&*_~©'''

for l in s:
    if l in punc:
        if l in dic.keys():
            dic[l] += 1
        else:
            dic[l] = 1

    

for l in s:
    if l in forb:
        s = s.replace(l, '')
        
arr = nltk.word_tokenize(s)

for word in arr:
    if word in dic.keys():
        dic[word]+=1
    else:
        dic[word] = 1
    
for i in range(len(arr)-1):
    li.append((str(arr[i]),str(arr[i+1])))
    

for t in li:
    if t in dicW.keys():
        dicW[t] +=1
    else:
        dicW[t] = 1

dicf = {}
#bugg double double to correct
for a,b in li:
    if a not in dicf.keys():
        listt = []
        listt.append((str(b),int(dicW[(a,b)])))
        dicf[a] = listt
    else:
        dicf[a].append((str(b),int(dicW[(a,b)])))

print(dicf)
f.close()

