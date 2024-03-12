from tkinter import *
from PIL import Image,ImageTk
from spellchecker import SpellChecker
class spell:
    def __init__(self,root):
        self.root = root
        self.bgj=Image.open('bgj.png')
        self.bgj=ImageTk.PhotoImage(self.bgj)
        self.bgj_lbl=Label(root,image=self.bgj)
        self.bgj_lbl.place(x=0,y=0)
        self.title_lbl=Label(root,text='SPELLING CHECKER',font=('Roboto', 15, 'bold'))
        self.title_lbl.place(x=180,y=0)
        self.name_entry=Entry(root,width=15,font=('Roboto', 15, 'bold'))
        self.name_entry.place(x=300,y=100)
        self.name_lbl=Label(root,text='Enter a refernce word : ',font=('Roboto', 15, 'italic'))
        self.name_lbl.place(x=50,y=100)
        self.submit_btn=Button(root,text='submit',font=('Roboto', 15),justify='center',command=self.register)
        self.submit_btn.place(x=250,y=300)
       
    def register(self):
        entered_word = self.name_entry.get()
        self.title_lbl.destroy()
        self.name_entry.destroy()
        self.name_lbl.destroy()
        self.submit_btn.destroy()
        spell_checker = SpellChecker()
        corrected_word = spell_checker.correction(entered_word)
        self.corr_word = Label(self.root, text='Correct spelling: ' + corrected_word, font=('Roboto', 15, 'bold'))
        self.corr_word.place(x=50, y=150)
root = Tk()
root.geometry('600x400+400+150')
root.title('spell')
lms = spell(root)
root.mainloop()