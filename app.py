from tkinter import *
from tkinter import ttk #This module provides classes to allow using Tk themed widget set.
from mainMethods import MyTranslator
app = Tk()
app.geometry("350x520")
app.title("Google Translator")
app.resizable(0,0)
app.config(bg='LIGHTSEAGREEN')
#app.wm_iconbitmap('icon.ico')

def get1():
    s= srcLangs.get() #get text from textarea
    d = desLangs.get()
    Sentence= sourceText.get(1.0,END)
    #object of Mytranslator class
    translator = MyTranslator()
    #calling the run method
    text = translator.run(txt=Sentence,src =s, dest=d)
    destText.delete(1.0,END) #clear the textarea
    destText.insert(END,text) #showing output

appName = Label(app,text="My Translator",font=('times new roman',20),
            bg='TEAL',fg='white',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
#creating frame
frame=Frame(app).pack(side=BOTTOM)
# textarea1 for taking input from user :Text is class
sourceText = Text(frame,font=('arial', 10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)
#btn
transBtn = Button(frame,text="Translate",font=('arial',10,'bold'),
            fg='white',bg='TEAL', activebackground='LIGHTSEAGREEN',relief=GROOVE,command=get1)
transBtn. pack(side=TOP,pady=15)
#set language
#langs = ['english','hindi','punjabi']
langs = MyTranslator().langs          

#dropdown list for input
srcLangs = ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=30,y=280)
srcLangs.set("English")
#dropdown list for output
desLangs = ttk.Combobox(frame,values=langs,width=10)
desLangs.place(x=240,y=280)
desLangs.set("Hindi")
# textarea2 for  output 
destText = Text(frame,font=('arial', 10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)

app.mainloop()