from tkinter import *
from googletrans import Translator
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("800x400")
root.title("Translator")
root.configure(background="black")
root.wm_iconbitmap("web_file.ico")


def Translation():
    
    word = user_variable.get()
    translator = Translator(service_urls=['translate.google.com'])
    Translation1 = translator.translate(word,dest="gu")
    l1.insert(END,f"translate in Gujarati:-{Translation1.text}")

def clr():
    l1.delete(0,END)


def about():
    tmsg.showinfo("About","We are Working for STARK INDUSTRIES\nDeveloped By Snehal Bhoya\nVersion- 1.0.1.12.0")

def contact():
    tmsg.showinfo("Contact us","Email:bhoyasnehal08@gmail.com\nMo:7405105079")

def feedback():
    ans = tmsg.askquestion("Rate us","how about our Service")

    if ans == "yes":

        tmsg.showinfo("Go on Store","Thanx for vist our App pls go on Store and Rate us please")
    
    elif ans == "no":

        tmsg.showinfo("improve","Owk We will learn about it and we will improve Soon a Better Features Thank You have a good day")


user_variable = StringVar()

mainmenu = Menu(root)
m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="About",command=about)
m1.add_command(label="Contactme",command=contact)
m1.add_command(label="Feedback",command=feedback)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="About us",menu=m1)


l1 = Label(root,text="Enter your Sentence",font="Courier 15 bold",bg="black",fg="cyan2")
l1.pack()

scrollbar_1 = Scrollbar(root,orient=HORIZONTAL)
Entry(root,textvariable=user_variable,bg="black",fg="green2",font="lucida 15 bold",width=40).pack()
Button(root,text="Translate",command=Translation,bg="dark orange").pack()

scrollbar_1.pack(side=BOTTOM,fill=X)
l1=Listbox(root,width=150, height=10,bg="black",fg="green2",xscrollcommand=scrollbar_1,font="lucida 15 bold")
l1.pack()
scrollbar_1.config(command=l1.xview)
Button(text="Clear",command=clr,bg="orange").pack()
root.mainloop()

