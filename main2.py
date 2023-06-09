from tkinter import*
from PIL import Image, ImageTk
root=Tk()
root.title("canvas example")
canvas=Canvas(root,width=400,height=600,bg="green")


canvas.create_rectangle(0,0,400,70,fill="blue")
canvas.create_oval(10,5,390,65,fill="black",outline="yellow",width=2)
canvas.create_text(200,30,text="hello i am rahul kumar",font="Times 20 italic bold",fill="red")
canvas.create_line(0,80,400,80,fill="white",width=10)

# photo=PhotoImage(file="Lord-Shiva.gif")
# canvas.create_image(0,90,image=photo,anchor=NW)

#Load an image in the script
img= (Image.open("Lord-Shiva.gif"))

#Resize the Image using resize method
resized_image= img.resize((385,300), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,90, anchor=NW, image=new_image)
canvas.create_rectangle(10,400,395,590,fill="white")
canvas.create_text(150,450,text="Name=Rahul Rahul",font="Times 20 italic bold",fill="black")
canvas.create_text(160,480,text="Reg No=20BCE10063",font="Times 20 italic bold",fill="black")
canvas.create_text(130,510,text="Program=B.Tech",font="Times 20 italic bold",fill="black")
canvas.create_text(105,540,text="Branch=CSE",font="Times 20 italic bold",fill="black")

canvas.pack()
root.mainloop()

