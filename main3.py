from tkinter import*
from PIL import Image, ImageTk
def movies():
    x = input("enter any move name for getting details(a,b,c)")
    if x == "a":
        print("details of movie a")
        root = Tk()
        root.title("canvas example")
        canvas = Canvas(root, width=400, height=600, bg="green")

        canvas.create_rectangle(0, 0, 400, 70, fill="blue")
        canvas.create_oval(10, 5, 390, 65, fill="black", outline="yellow", width=2)
        canvas.create_text(200, 30, text="3-Idiots is a 2009 Indian", font="Times 20 italic bold", fill="red")
        canvas.create_line(0, 80, 400, 80, fill="white", width=10)

        # photo=PhotoImage(file="Lord-Shiva.gif")
        # canvas.create_image(0,90,image=photo,anchor=NW)

        # Load an image in the script
        img = (Image.open("3_idiots_poster.jpg"))

        # Resize the Image using resize method
        resized_image = img.resize((385, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        # Add image to the Canvas Items
        canvas.create_image(10, 90, anchor=NW, image=new_image)
        canvas.create_rectangle(10, 400, 395, 590, fill="white")
        canvas.create_text(175, 450, text="Producer=Vinod Chopra", font="Times 20 italic bold", fill="black")
        canvas.create_text(180, 480, text="Director=Rajkumar Hirani", font="Times 20 italic bold", fill="black")
        canvas.create_text(170, 510, text="Writer=Rajkumar Hirani", font="Times 20 italic bold", fill="black")
        canvas.create_text(190, 540, text="Stars=Amir khan,Madhavan", font="Times 20 italic bold", fill="black")

        canvas.pack()
        root.mainloop()

    elif x == "b":
        print("details of movie b")
        root = Tk()
        root.title("canvas example")
        canvas = Canvas(root, width=400, height=600, bg="green")

        canvas.create_rectangle(0, 0, 400, 70, fill="blue")
        canvas.create_oval(10, 5, 390, 65, fill="black", outline="yellow", width=2)
        canvas.create_text(200, 30, text="Taare Zameen Par", font="Times 20 italic bold", fill="red")
        canvas.create_line(0, 80, 400, 80, fill="white", width=10)

        # photo=PhotoImage(file="Lord-Shiva.gif")
        # canvas.create_image(0,90,image=photo,anchor=NW)

        # Load an image in the script
        img = (Image.open("Taare_Zameen_Par.png"))

        # Resize the Image using resize method
        resized_image = img.resize((385, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        # Add image to the Canvas Items
        canvas.create_image(10, 90, anchor=NW, image=new_image)
        canvas.create_rectangle(10, 400, 395, 590, fill="white")
        canvas.create_text(170, 450, text="Producer=Amir khan", font="Times 20 italic bold", fill="black")
        canvas.create_text(161, 480, text="Director=Amir khan", font="Times 20 italic bold", fill="black")
        canvas.create_text(160, 510, text="Writer=Amole gupte", font="Times 20 italic bold", fill="black")
        canvas.create_text(190, 540, text="Stars=Amir khan,Darsheel", font="Times 20 italic bold", fill="black")

        canvas.pack()
        root.mainloop()
    elif x == "c":
        print("details of movie c")
        root = Tk()
        root.title("canvas example")
        canvas = Canvas(root, width=400, height=600, bg="green")

        canvas.create_rectangle(0, 0, 400, 70, fill="blue")
        canvas.create_oval(10, 5, 390, 65, fill="black", outline="yellow", width=2)
        canvas.create_text(200, 30, text="hello i am rahul kumar", font="Times 20 italic bold", fill="red")
        canvas.create_line(0, 80, 400, 80, fill="white", width=10)

        # photo=PhotoImage(file="Lord-Shiva.gif")
        # canvas.create_image(0,90,image=photo,anchor=NW)

        # Load an image in the script
        img = (Image.open("Lord-Shiva.gif"))

        # Resize the Image using resize method
        resized_image = img.resize((385, 300))
        new_image = ImageTk.PhotoImage(resized_image)

        # Add image to the Canvas Items
        canvas.create_image(10, 90, anchor=NW, image=new_image)
        canvas.create_rectangle(10, 400, 395, 590, fill="white")
        canvas.create_text(150, 450, text="Name=Rahul Rahul", font="Times 20 italic bold", fill="black")
        canvas.create_text(160, 480, text="Reg No=20BCE10063", font="Times 20 italic bold", fill="black")
        canvas.create_text(130, 510, text="Program=B.Tech", font="Times 20 italic bold", fill="black")
        canvas.create_text(105, 540, text="Branch=CSE", font="Times 20 italic bold", fill="black")

        canvas.pack()
        root.mainloop()
    else:
        print("please enter valid input")
        movies()



while True:
    n=input("enter y/n for starting:")

    if n=="y":
        movies()

    elif n=="n":
        print("-------thanks you visit-------")
        break
    else:
        print("please enter valid input")
