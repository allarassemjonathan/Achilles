from random import random
def MarkovChains():
    dic = {}
    dicW = {}
    li = []
    total = 0
    punc = '.!'
    p = []
    w = ''
    temp = ''
    forb = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°‘()-—[]{};:'“”"«»\,+<>./?@#$%^&*_~©'''
    f = open(r'C:\Users\ALLARASSEMJJ20\Achilles\Frankeshtein.txt', encoding = 'utf-8')
    string = f.read()
    s = string
           
    for l in s:
        if l in punc:
            if l in dic.keys():
                dic[l] += 1
            else:
                dic[l] = 1

    s = s.replace('.',' ')
    s = s.replace('!',' ')
    for l in s:
        if l in forb:
            s = s.replace(l, '')
    print(s)
    arr = s.split()
    for i in range(len(arr)-1):
        li.append((str(arr[i]),str(arr[i+1])))
        
    print(arr)
    for t in li:
        if t in dicW.keys():
            dicW[t] +=1
        else:
            dicW[t] = 1
           
    dicF = {}
    for a,b in li:
        if a not in dicF.keys():
                dictemp = {}
                dictemp[str(b)] = float(dicW[(a,b)])
                dicF[a] = dictemp
        else:
                
                dictemp = dicF[a]
                dictemp[str(b)] = float(dicW[(a,b)])
                dicF[a] = dictemp
                
    for k1 in dicF.keys():
            total = 0
            for k2 in dicF[k1].keys():
                total += dicF[k1][k2]
            for k2 in dicF[k1].keys():
                dicF[k1][k2] /= total
                
    print(dicF)
    
def GenerativeModel():
    sentence = ''
    n = int(random()*len(dicF))
    sentence += dic[arr[n]] + ' '
    
    
    
    

MarkovChains()
