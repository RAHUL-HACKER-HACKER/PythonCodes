from tkinter import*
root=Tk()
root.title("hello")
root.geometry("250x300")
Label(root,text="student",bg="red").place(x=10,y=20)
Entry(root).place(x=80,y=20)
Label(root,text="course",fg="red").place(x=10,y=40)
Entry(root).place(x=80,y=40)
Button(root,text="click here").place(x=100,y=100)




root.mainloop()