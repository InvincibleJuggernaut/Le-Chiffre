from tkinter import *

window =Tk()
window.resizable(width=False, height=False)
window.title("Le Chiffre")
window.geometry('700x700')
window.configure(bg="black")

lb1=Label(window, text="Le Chiffre", bg="#282828", fg="white", font=("Roboto", 30), padx=10, pady=10)
lb1.place(relx=.5, rely=.1,anchor="center")

textbox_1 = Text(window, height=8, width=35, font="Roboto 13")
textbox_2 = Text(window, height=8, width=35, font="Roboto 13")
convert_button = Button(window, text='Convert')

textbox_1.place(relx=.5, rely=.4, anchor="center")
textbox_2.place(relx=.5, rely=.8, anchor="center")
convert_button.place(relx=.5, rely=.6, anchor="center")

window.mainloop()

