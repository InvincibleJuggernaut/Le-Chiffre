from tkinter import *

window =Tk()
window.resizable(width=False, height=False)
window.title("Le Chiffre")
window.geometry('700x700')
window.configure(bg="black")

lb1=Label(window, text="Le Chiffre", bg="#282828", fg="white", font=("Roboto", 30), padx=10, pady=10)
lb1.place(relx=.5, rely=.1,anchor="center")

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

spaces=[]

def clear():
    textbox_1.delete(1.0, END)
    textbox_2.delete(1.0, END)
    textbox_3.delete(1.0, END)

def encrypt():
    option='e'
    msg = textbox_1.get("1.0", "end")[:-1]
    key = textbox_2.get("1.0", "end")[:-1]
    
    for i in range(0, len(msg)):
        if msg[i] == ' ':
            spaces.append(i)
            
    msg = ''.join(msg.split())
    
    print(msg)
    print(type(msg))
    if(len(key)<len(msg)):
        new_key = key*len(msg)
        new_key = new_key[0:len(msg)]

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
    
    for x in spaces:
        w.insert(x, ' ')    
    
    w = ''.join(str(x) for x in w)
    
    textbox_3.delete(1.0, END)
    textbox_3.insert('end -1 chars', w)

def decrypt():

    option='d'
    msg = textbox_1.get("1.0", "end")[:-1]
    key = textbox_2.get("1.0", "end")[:-1]
    
    msg = ''.join(msg.split())

    if(len(key)<len(msg)):
        new_key = key*len(msg)
        new_key = new_key[0:len(msg)]

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
    
    for x in spaces:
        w.insert(x, ' ')
        
    w = ''.join(str(x) for x in w)
    
    textbox_3.delete(1.0, END)
    textbox_3.insert('end -1 chars', w)
    
    
textbox_1 = Text(window, height=4, width=35, font="Roboto 13")
textbox_2 = Text(window, height=1, width=35, font="Roboto 13")
textbox_3 = Text(window, height=4, width=35, font="Roboto 13")

radio_button1 = Radiobutton(window, text='Encrypt', variable='answer', value=1, command=encrypt)
radio_button2 = Radiobutton(window, text='Decrypt', variable='answer', value=2, command=decrypt)

clear_button = Button(window, text='Clear', command=clear)

textbox_1.place(relx=.5, rely=.3, anchor="center")
textbox_2.place(relx=.5, rely=.45, anchor="center")
textbox_3.place(relx=.5, rely=.7, anchor="center")

#textbox_1.insert('end -1 chars','Enter the plaintext or ciphertext here')
#textbox_2.insert('end -1 chars', 'Enter the key here')

radio_button1.place(relx=.45, rely=.55, anchor="center")
radio_button2.place(relx=.55, rely=.55, anchor="center")
clear_button.place(relx=.5, rely=.87, anchor="center")

window.mainloop()
