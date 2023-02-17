#Libraries
from tkinter import *
from tkinter import messagebox,colorchooser
from tkinter.font import Font
from textblob import TextBlob

#Application setup
root = Tk()
root.title("Spelling Checker")
root.geometry("700x400+280+60")
root.resizable(False,False)
root.configure(bg="#dae6f6")

#Functions
def check_spelling():
    word = e1.get()
    if(word==""):
        messagebox.showwarning("Blank","Nothing to be filled here !!!")
    else:
        a = TextBlob(word)
        right = str(a.correct())
        global cs
        cs = Label(root,text="Correct text is: ",font=("poppins",20,"bold"),fg="#364971",bg="#dae6f6")
        cs.place(x=100,y=250)
        spell_check.config(text=right)

def color(event):
    cls = colorchooser.askcolor(title="Select color to change")
    root.configure(bg=cls[1])
    l1.config(bg=cls[1])
    btn.config(bg=cls[1])
    spell_check.config(bg=cls[1])
    cs.config(bg=cls[1])


#Application creation
img1 = PhotoImage(file="E:\\pyImages\\spell_logo.png")
root.iconphoto(False,img1)
l1 = Label(root,text="Spelling Checker",font=Font(family="Trebuchet MS",
        weight="bold",size=30),bg="#dae6f6",fg="#364971")
l1.pack(pady=(50,0))
e1 = Entry(root,justify="center",width=30,bd=2,bg="white",fg="black",
            font=Font(family="poppins",weight="bold",size=25))
e1.pack(pady=10); e1.focus()
btn = Button(root,text="Check",bg="light green",activebackground="light green",fg="black",bd=4,
            font=Font(family="Algerian",weight="bold",size=20),cursor="hand2",command=check_spelling)
btn.pack()
spell_check = Label(root,font=("poppins",20,"bold"),bg="#dae6f6",fg="#364971")
spell_check.place(x=350,y=250)
root.bind('<Control-g>',color)
root.mainloop()