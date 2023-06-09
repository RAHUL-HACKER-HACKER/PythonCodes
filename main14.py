from tkinter import*
#
# def set():
#     selection=f"enjoy your {var.get()}"
#     label.cofig(test=selection)
#
# top=Tk()
# top.geometry("200x250")
# var=StringVar()
# r1=Radiobutton(top,text="pizza slice",variable=var,value="pizzza",command=sel)
# r1.pack(anchor=W)
# r2=Radiobutton(top,text="burger",variable=var,value="burger",command=sel)

def sel():

    selection = f'Enjoy your{var.get()}'


top = Tk()
top.geometry('500x500')
var = StringVar()
R1 = Radiobutton(top, text='pizza slice', variable=var, value='pizza', command=sel())
R1.pack(anchor=W)
R2 = Radiobutton(top, text='fries', variable=var, value='fries', command=sel())
R2.pack(anchor=W)

top.mainloop()