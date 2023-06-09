from tkinter import*
from tkinter import messagebox
top=Tk()
top.title("messagebox")
def clickhere():
    messagebox.showinfo("click here","you just gone own")

button=Button(top,text="click here",command=clickhere)
button.place(x=75,y=100)
top.mainloop()