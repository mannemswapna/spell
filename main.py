from tkinter import *
class LMS:
    def __init__(self,root) :
        self.title_lbl = Label(root,text= 'This is my app', font=('Times New Roman', 20, 'bold'))
        self.title_lbl.place(x=150,y=0)
        self.name_entry=Entry(root,width=15,font=('Times New Roman', 15, 'bold'))
        self.name_entry.place(x=150,y=100)
        self.name_lbl=Label(root,width=10,text= 'NAME', font=('Times New Roman', 20, 'bold'),justify='center')
        self.name_lbl.place(x=10,y=100)
        self.submit_btn=Button(root,text='SUBMIT',font=('Times New Roman', 20, 'bold'),justify='center')
        self.submit_btn.place(x=200,y=200)
root = Tk()
root.geometry('500x300+400+150')
root.title('my-app')
lms= LMS(root)
root.mainloop()