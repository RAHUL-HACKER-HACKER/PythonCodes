#prg to create an action over widgets
import tkinter as tk
window=tk.Tk()
def mhello():
    label1=tk.Label(window,text="hello,nice to meet you").pack()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="smschool")
    mycursor = mysqldb.cursor()


window.geometry("400x350")
window.title("create 3 widgets-label,textentry and button ")
tk.Label(text="----hello i am tkinter----",background="green").pack()
lbl_sample=tk.Label(window,text="Label")
txt_entry=tk.Entry(window)
btn_sample=tk.Button(window,text="click on it",command=mhello,fg="red")
lbl_sample.pack()
txt_entry.pack()
btn_sample.pack()



window.mainloop()