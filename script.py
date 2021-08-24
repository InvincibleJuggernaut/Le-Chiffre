option = input()
msg=input('Enter message : ')

key=input('Enter key : ')

if(len(key)<len(msg)):
    new_key = key*len(msg)
    new_key = new_key[0:len(msg)]

arr = {0:['A','a'],
1:['B','b'],
2:['C','c'],
3:['D','d'],
4:['E','e'],
5:['F','f'],
6:['G','g'],
7:['H','h'],
8:['I','i'],
9:['J','j'],
10:['K','k'],
11:['L','l'],
12:['M','m'],
13:['N','n'],
14:['O','o'],
15:['P','p'],
16:['Q','q'],
17:['R','r'],
18:['S','s'],
19:['T','t'],
20:['U','u'],
21:['V','v'],
22:['W','w'],
23:['X','x'],
24:['Y','y'],
25:['Z','z']
}

l=[]
first_half = 0
second_half = 0

for i in range(0, len(msg)):
    for key, value in arr.items():
        if(str(msg[i])==str(value[0]) or str(msg[i])==str(value[1])):
            first_half = key
        if(str(new_key[i])==str(value[0]) or str(new_key[i])==str(value[1])):
            second_half = key
        
    if(option == 'e'): 
        sum = int(first_half) + int(second_half)
    else:
        sum = int(first_half) - int(second_half)
    if(int(sum)>25):
        sum = sum%26
    if(int(sum)<0):
        sum += 26
    l.append(sum)

w=[]

for x in l:
    ct = arr.get(x)
    w.append(ct[0])    
    
print(w)
