from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, width
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from diskschedulingAlgorithms import FCFS, SSTF, SCAN, CSCAN, LOOK, CLOOK
import time, turtle
from Exceptions import Error,itemGreater, itemMany

class Process:
    def __init__(self,root):
        self.root = root
        self.root.title("Disk Scheduling System")
        self.root.geometry("600x500+300+100")
        self.root.resizable(0,0)
        self.root.config(bg='gray')

        #self.bg = ImageTk.PhotoImage(file="images/bgimage.jpg")
        #self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

        self.frame1 = LabelFrame(self.root, width=600, height=500, bg='white', bd=5, relief=SUNKEN)
        self.frame1.pack(padx=10, pady=20)


        #frame1 = Frame(self.frame1)
        Label(self.frame1, text='Algorithm: ', bg='white', font = ('Helvetica',12,'bold')).place(x=175, y=25)
        self.algMenu = ttk.Combobox(self.frame1,values=['FCFS', 'SSTF', 'SCAN','CSCAN', 'LOOK', 'CLOOK'])
        self.algMenu.place(x=275, y=25)
        self.algMenu.current(0)

        self.timeScale = Scale(self.frame1, from_=0.0, to=6.0, length=200, digits=2, resolution=2.0, 
                orient=HORIZONTAL, label="Select Speed [s]", font=('Helvetica',12, 'bold'))
        self.timeScale.place(x=175, y=85)

        Label(self.frame1, text='Input Values: ', bg='white', font = ('Helvetica',12,'bold')).place(x=175, y=180)
        self.inputValues = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.inputValues.place(x=175, y=210)
        self.inputValues.insert(0, "data seperated by space")
        self.inputValues.bind("<Button>",self.userText)

        Label(self.frame1, text='Current Position of R/W Head: ', bg='white', font = ('Helvetica',
        12,'bold')).place(x=175, y=265)
        self.posiionHead = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.posiionHead.place(x=175, y=295)

        #home button
        home_btn = Button(self.frame1, text="Home", command=self.back_2_home , relief=GROOVE, bd=4,cursor="hand2",
         bg="sandy brown", fg="white",width=10, font=("times new roman", 13, "bold")).place(x=130, y=360)

        #reset button
        reset_btn = Button(self.frame1, text="Reset", command=self.reset , relief=GROOVE, bd=4, cursor="hand2", 
        bg="red", fg="white",width=10, font=("times new roman", 13, "bold")).place(x=230, y=360)

        #visualize button
        start_btn = Button(self.frame1, text="Visualize", command=self.Visualise, bd=4, relief=GROOVE,
         cursor="hand2", bg="green",fg="white",width=10, font=("times new roman", 13, "bold")).place(x=340, y=360)

    
    def userText(self, event):
        self.inputValues.delete(0, END)

    def reset(self):
        self.inputValues.delete(0,END)
        self.posiionHead.delete(0,END)

    def back_2_home(self):
        self.root.destroy()


    def Visualise(self):
        
        try:
            request_arr = self.inputValues.get()
            option = self.algMenu.get()
            start = int(self.posiionHead.get())
            timeSpeed = self.timeScale.get()
            #print(timeSpeed)
            request=(request_arr.split(sep=" "))
            request=[int(i) for i in request]
            
            if len(request) > 15:
                raise itemMany
            
            for x in range(len(request)):
                if request[x] > 200 or start > 200 :
                    raise itemGreater

            # Select and run algorithm
            if option == "FCFS":                       
                Order, Sum = FCFS(request, start)
            elif option =="SSTF":
                Order, Sum = SSTF(request, start)
            elif option =="SCAN":
                Order, Sum = SCAN(request, start)
            elif option =="CSCAN":
                Order, Sum = CSCAN(request, start)
            elif option =="LOOK":
                Order, Sum = LOOK(request, start)
            elif option =="CLOOK":
                Order, Sum = CLOOK(request, start)

            #turtle screen
            timeStart = time.time()
            turtle.clearscreen()
            diskWin = turtle.Screen()
            diskWin.title(option)
            diskWin.bgcolor("white")

            # Set turtle window boundaries
            diskWin.setworldcoordinates(-5, -20, 210, 10)

            #square box in each circle
            squareBox = turtle.Turtle()
            squareBox.shape("square")
            squareBox.color("black")
            squareBox.turtlesize(.3, .3, 1)
            squareBox.speed(timeSpeed)
            squareBox.pensize(0)

            #circle for indexing numbers in a timeline
            circleFig = turtle.Turtle()
            circleFig.shape("circle")
            circleFig.color("green")
            circleFig.turtlesize(.3, .3, 1)
            circleFig.speed(timeSpeed)
            circleFig.pensize(0)

            n = len(Order)
            y = -1
            y2=0
            temp_order=[int(i*10) for i in range(0,21)]
            for i in range(0,len(temp_order)):
                circleFig.goto(temp_order[i], y2)
                circleFig.stamp()
                circleFig.write(temp_order[i], False, align="right")

            for i in range(0, n):
                if i == 0:      # No drawing while the disksquareBox reaches start position
                    squareBox.penup()
                    squareBox.goto(Order[i], y)
                    squareBox.pendown()
                    squareBox.stamp()
                    squareBox.write(Order[i], False, align="right")
                else:           # DisksquareBox draws its path to each request
                    squareBox.goto(Order[i], y-1)
                    squareBox.stamp()
                    squareBox.write(Order[i], False, align="right")
                    y -= 1
            squareBox.hideturtle()
            squareBox.speed(timeSpeed)
            squareBox.penup()
            timeEnds = time.time()

            message1 = "Disk Scheduling Algorithm: " + option
            message2 = "Total Head Movement: " + str(Sum)

            #Display input Data
            squareBox.goto(100,9)
            squareBox.color("black")
            squareBox.write("Input Data: "+ str(request) , False,
            align="left",font=("New Times Roman", 13,'bold') )

            
            # Display algorithm used
            squareBox.goto(100, 7)
            squareBox.color("magenta")
            squareBox.write(message1, False, align="left",font=("Courier", 13, 'bold'), )   
            
            # Display total movement
            squareBox.goto(100,5)
            squareBox.color("red")
            squareBox.write(message2, False, align="left",font=("Arial", 13,'bold') )     
            
            #Display time taken to complete the algorithm
            squareBox.goto(100,3)
            squareBox.color("cyan")
            squareBox.write("Time taken: "+str(round(timeEnds-timeStart, 2))+" Seconds", False,
            align="left",font=("Helvetica", 13,'bold') )

            squareBox.pendown
            diskWin.exitonclick()

        except ValueError:
            messagebox.showerror("Error",
                            "Please provide valid array seperated by space",parent=self.root)
            self.inputValues.delete(0, END)
            self.posiionHead.delete(0,END)

        except itemMany:
            messagebox.showerror("Error",
                            "Length of Input Data should be less than 15",parent=self.root)
            self.inputValues.delete(0, END)

        except itemGreater:
            messagebox.showerror("Error",
                            "Input Data should be between 0 and 200",parent=self.root)
            self.inputValues.delete(0, END)
            self.posiionHead.delete(0,END)


root = Tk()
obj = Process(root)
root.mainloop()