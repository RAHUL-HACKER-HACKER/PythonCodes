import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector


def movies_database():
    reviewer = e1.get()
    movies = e2.get()
    rating = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="7261888792", database="pycharmDatabase")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO movies_rating (reviewer,movies,rating) VALUES (%s, %s, %s)"
        val = (reviewer, movies, rating)
        mycursor.execute(sql, val)
        mysqldb.commit()
        messagebox.showinfo("information", "Record inserted successfully...")


    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


root = Tk()
root.title("MOVIES RATING")
root.geometry("300x200")
icon=tkinter.PhotoImage(file="college.gif")
#root.config(bg="red")
label=tkinter.Label(root,image=icon)
label.pack()
global e1
global e2
global e3
# l0 = Label(root, text='movies rating details',
#               font=('Helvetica', 16), width=30, anchor="c").pack()
# l0.grid(row=1, column=1, columnspan=4)
Label(root, text="REVIEWER" ,bg="orange").place(x=10, y=10)
Label(root, text="MOVIE",bg="orange").place(x=10, y=40)
Label(root, text="RATING",bg="orange").place(x=10, y=80)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=80)

Button(root,fg="black",bg="purple", text="submit", command=movies_database, height=3, width=13).place(x=100, y=120)

root.mainloop()