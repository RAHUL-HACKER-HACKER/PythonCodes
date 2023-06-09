from tkinter import*
top=Tk()
top.geometry("350x400")
top.title("hello i am chackbutton")
top.configure(bg='yellow')
checkvar1=IntVar()
checkvar2=IntVar()

c1=Checkbutton(top,text="pizzz",variable=checkvar1,onvalue=1,offvalue=0,height=10,width=10)
c2=Checkbutton(top,text="fries",variable=checkvar2,onvalue=1,offvalue=0,height=20,width=20)
c1.pack()
c2.pack()
top.mainloop()

