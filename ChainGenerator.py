s = 'I go to the beach. I took a sandwich. I am doing very well. See you guys'
arr = s.split()
p = '.!'
for i in range(len(arr)-1):
    if arr[i][len(arr[i])-1] in p and len(arr[i])-1>0:
        arr.insert(i+1, arr[i][len(arr[i])-1])
        arr[i] = arr[i][0:len(arr[i])-1]
        
print(arr)
        
