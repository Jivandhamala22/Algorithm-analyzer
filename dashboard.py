from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from os import sep
from tkinter import messagebox
from searchingAlgorithm import binarySearch, linearSearch
from sortingAlgorithms import BubbleSort, merge_sort, QuickSort
from turtle import bgcolor, width
from diskschedulingAlgorithms import FCFS, SSTF, SCAN, CSCAN, LOOK, CLOOK
import time, turtle
from Exceptions import *
import pymysql,re, time

import random

class HomePage:
    def __init__(self,root):
        self.root = root
        self.root.title('Algorithm Visualizer')
        #root.iconbitmap("images/algologo.ico")
        self.root.geometry("900x620+200+20")
        self.root.resizable(0,0)
        self.root.config(bg='black')

        #first menu frame
        frame1 = Frame(self.root, width=900, height=180, bg='black', bd = 2 , relief = SUNKEN)
        frame1.pack()
        label1 = Label(frame1,text = 'Enjoy the new way of studying algorithms',font = ('Helvetica',12,'bold')
            ,fg = 'white',bg = 'black')
        label1.place(x = 280 , y = 35)
        label1 = Label(frame1,text = 'Algorithm Analyzer',font = ('Helvetica',18,'bold')
            ,fg = 'white',bg = 'black')
        label1.place(x = 330 , y = 75)
        label1 = Label(frame1,text = 'Choose from below algorithms to get started',font = ('Helvetica',12,'bold')
            ,fg = 'white',bg = 'black')
        label1.place(x = 280 , y = 125)

        btnhome = Button(frame1 , text = ' Home ' , font = ('New Times Roman',11,'bold') ,bg = 'sandy brown',
        fg = 'white', bd='4',relief=SUNKEN, command=self.homeWindow, activebackground='green', activeforeground='white')
        btnhome.place(x = 635 , y = 15)
        btncontact = Button(frame1 , text = ' About ' , font = ('New Times Roman',11,'bold') ,bg = 'sky blue',
        fg = 'white',bd='4', relief=SUNKEN, activebackground='green', activeforeground='white', command=self.aboutWindow)
        btncontact.place(x = 715 , y = 15)
        btnlogin = Button(frame1 , text = ' Login ' ,command=self.loginWindow,  font = ('New Times Roman',11,'bold')
        ,bg = 'Blue',fg = 'white',bd='4', relief=SUNKEN, activebackground='green', activeforeground='white')
        btnlogin.place(x = 795 , y = 15)

        #second frame for description where we add scrollbar
        frame2 = Frame(self.root)
        frame2.pack(fill=BOTH, expand=1)

        #canvas for scrolling
        my_canvas = Canvas(frame2)
        my_canvas.pack(side=LEFT, fill=BOTH, expand = 1)

        #scrollbar for displaying description
        scrollBar = Scrollbar(frame2, orient=VERTICAL, command=my_canvas.yview)
        scrollBar.pack(side=RIGHT, fill=Y)

        #configure scrollbar
        my_canvas.configure(yscrollcommand=scrollBar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        #creating another frame inside the canvas
        canvas_frame = Frame(my_canvas)

        #Adding that new frame to a window in the canvas
        my_canvas.create_window((0,0), window=canvas_frame, anchor="nw")

        #frames within frames for sorting , scheduling and searching description
        frameSort = Frame(canvas_frame, width=440, height=440,bg='white', bd = 5 , relief = SUNKEN )
        frameSort.grid(row=0, column=0)
        frameSearch = Frame(canvas_frame, width=440, height=440,bg='white', bd = 5 , relief = SUNKEN )
        frameSearch.grid(row=0, column=1)
        frameSchedule = Frame(canvas_frame, width=440, height=440,bg='white', bd = 5 , relief = SUNKEN )
        frameSchedule.grid(row=1, column=0)
        frameProcess = Frame(canvas_frame, width=440, height=440,bg='white', bd = 5 , relief = SUNKEN )
        frameProcess.grid(row=1, column=1)

        #for sorting image to be placed
        sorting_img = Image.open("images/sorting.gif")
        resized_sortingimg = sorting_img.resize((250,188) , Image.ANTIALIAS)
        imgsort = ImageTk.PhotoImage(resized_sortingimg)  # PIL solution
        imgsortlabel = Label(frameSort, image=imgsort, bg='white')
        imgsortlabel.photo = imgsort
        imgsortlabel.place(x=50, y=75)

        #for searching image to be placed
        searching_img = Image.open("images/searching.png")
        resized_searchimg = searching_img.resize((250,188) , Image.ANTIALIAS)
        imgsearch = ImageTk.PhotoImage(resized_searchimg)  # PIL solution
        imgsearchlabel = Label(frameSearch, image=imgsearch, bg='white')
        imgsearchlabel.photo = imgsearch
        imgsearchlabel.place(x=50, y=75)

         #for disk scheduli8ng image to be placed
        scheduling_img = Image.open("images/diskscheduling.png")
        resized_scheduleimg = scheduling_img.resize((250,188) , Image.ANTIALIAS)
        imgschedule = ImageTk.PhotoImage(resized_scheduleimg)  # PIL solution
        imgschedulelabel = Label(frameSchedule, image=imgschedule, bg='white')
        imgschedulelabel.photo = imgschedule
        imgschedulelabel.place(x=50, y=75)

        #buttons to go to the sorting window and searching window
        btnsort = Button(frameSort ,command = self.sorting_WIN, text = 'Click Here to Get Started' , font = (' Helvetica',11,'bold')
            ,bg = 'black',fg = 'white', relief=SUNKEN,bd='5' )
        btnsort.place(x = 100 , y = 335)
        btnsearch = Button(frameSearch ,command = self.searching_WIN,  text = 'Click Here to Get Started' , font = ('Helvetica',11,'bold')
              ,bg = 'black',fg = 'white',bd='5', relief=SUNKEN)
        btnsearch.place(x = 100 , y = 335)
        btndisk = Button(frameSchedule ,command = self.diskschedule_WIN,  text = 'Click Here to Get Started' , font = ('Helvetica',11,'bold')
              ,bg = 'black',fg = 'white',bd='5', relief=SUNKEN)
        btndisk.place(x = 100 , y = 335)

    def homeWindow(self):
        pass

    def aboutWindow(self):
        turtle.clearscreen()
        aboutWin = turtle.Screen()
        aboutWin.title("About Algorithm Analyzer")
        aboutWin.bgcolor("white")
        aboutWin.setworldcoordinates(-5, -20, 210, 10)

        console = turtle.Turtle()
        console.penup()
        console.color("Red")
        console.goto(70,9)
        console.write("Algorithm Analyzer.......",False, align="right",font=("Helvetica", 15, 'bold'))
        console.color("black")
        console.goto(200,7)
        console.write("This project contains some sorting, searching and disk scheduling algorithms ", False, align="right",font=("New Times Roman", 13, 'bold'))
        console.goto(150,6)
        console.write(" and here, we analyze all algorithms in graphical way......", False, align="right",font=("New Times Roman", 13, 'bold'))

        console.color("Green")
        console.goto(100,1)
        console.write("Made By:", False, align='right',font=("Times New Roman", 15,'bold'))
        console.color("black")
        console.goto(110,-0.5)
        console.write("Jeewan Dhamala", False, align='right',font=("Times New Roman", 14,'bold'))
        console.goto(105,-1.5)
        console.write("Jitendra Tharu", False, align='right',font=("Times New Roman", 14,'bold'))
        console.goto(100,-2.5)
        console.write("Saroj Basnet", False, align='right',font=("Times New Roman", 14,'bold'))
        console.pendown
        aboutWin.exitonclick()

    def diskschedule_WIN(self):
        class DiskScheduling:
            def __init__(self,diskscheduleWin):
                self.diskscheduleWin = diskscheduleWin
                self.diskscheduleWin.title("Disk Scheduling System")
                self.diskscheduleWin.geometry("600x500+300+100")
                self.diskscheduleWin.resizable(0,0)
                self.diskscheduleWin.config(bg='gray')

                #self.bg = ImageTk.PhotoImage(file="images/bgimage.jpg")
                #self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

                self.frame1 = LabelFrame(self.diskscheduleWin, width=600, height=500, bg='white', bd=5, relief=SUNKEN)
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
                self.diskscheduleWin.destroy()


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
                                    "Please provide valid array seperated by space",parent=self.diskscheduleWin)
                    self.inputValues.delete(0, END)
                    self.posiionHead.delete(0,END)

                except itemMany:
                    messagebox.showerror("Error",
                                    "Length of Input Data should be less than 15",parent=self.diskscheduleWin)
                    self.inputValues.delete(0, END)

                except itemGreater:
                    messagebox.showerror("Error",
                                    "Input Data should be between 0 and 200",parent=self.diskscheduleWin)
                    self.inputValues.delete(0, END)
                    self.posiionHead.delete(0,END)

        diskscheduleWin = Toplevel(self.root)
        obj = DiskScheduling(diskscheduleWin)
        diskscheduleWin.mainloop()

    def searching_WIN(self):
        class Searching:
            def __init__(self,searching_win):
                self.searching_win = searching_win
                #----------window---------
                self.searching_win.title('Algorithm Visualizer')
                self.searching_win.geometry("900x620+200+20")
                self.searching_win.resizable(0,0)
                self.searching_win.config(bg='black')

                self.top_frame = Frame(self.searching_win, width=900, height=200, bg='grey', bd=2, relief=SUNKEN)
                self.top_frame.grid(row=0, column=0, padx=10, pady=5)
                self.canvas = Canvas(self.searching_win, width=890, height=450, bg='white', bd=5, relief=GROOVE)
                self.canvas.grid(row=1, column=0, pady=5)

                Label(self.top_frame, text='Algorithm: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=W)
                self.algMenu = ttk.Combobox(self.top_frame,values=['Binary Search', 'Linear Search'])
                self.algMenu.grid(row=0, column=1, pady=5)
                self.algMenu.current(0)

                Label(self.top_frame, text='Item to be Searched', bg='grey', font = ('Helvetica',12,'bold')).place(x=550,y=68)
                self.itemsearchEntry = Entry(self.top_frame, bd = 5 , relief = GROOVE,width = 7)
                self.itemsearchEntry.place(x = 545, y=95, height=38)
                self.itemsearchEntry.bind("<Button>",self.clearText)
                Button(self.top_frame, text='  Start   ', command=self.StartAlgorithm , bg='red', font = ('New Times Roman',10,'bold'), bd='4').place(x=630, y=100)

                self.timeScale = Scale(self.top_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
                self.timeScale.grid(padx=15, pady=5, row=0, column=2)

                Label(self.top_frame, text='Input: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=1, column=0, padx=15, pady=5, sticky=W)
                self.inputEntry = Entry(self.top_frame, bd = 5 , relief = GROOVE,width = 30)
                self.inputEntry.grid(row=1, column=1,  pady=5, sticky=W)
                self.inputEntry.insert(0, "sorted array seperated by space")
                self.inputEntry.bind("<Button>",self.userText)

                #Label(self.top_frame, text='Max-Size: ', bg='grey').grid(row=1, column=2, padx=15, pady=5, sticky=W)
                #inputaEntry = Entry(self.top_frame,bd = 5 , relief = GROOVE,width = 25)
                #inputaEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                        #Label for showing the searched element index
                self.label_itemfound = Label(self.canvas, text=" ", bg="white", fg="green",
                                            font=("Helvetica", 13, 'bold'))
                self.label_itemfound.place(x=600, y=70)

                # Label for showing no of comparisons
                self.label_index = Label(self.canvas, text="  ", bg="white", fg="light salmon",
                                            font=("Helvetica", 13, 'bold'))
                self.label_index.place(x=600, y=10)

                # Label for showing execution time
                self.label_time = Label(self.canvas, text="  ", bg="white", fg="medium blue",
                                            font=("Helvetica", 13, 'bold'))
                self.label_time.place(x=600, y=40)

                # button for going back to home page
                Button(self.top_frame, text='  Home   ', command=self.back_2_home, font = ('New Times Roman',11,'bold')
                                ,bg = 'sandy brown',fg = 'white', bd='2',relief=SUNKEN).grid(row=0, column=5, padx=80)

                Button(self.top_frame, text='  Generate  ', command=self.Generate, bg='cyan', font = ('New Times Roman',10,'bold'), bd='4').grid( row=1, column=2, pady=20)


            def Generate(self):
                self.canvas.delete('all')
                print('Algorithm selected: '+ self.algMenu.get())
                global inputArray

                try:
                    if self.inputEntry.get() == "sorted array seperated by space" :
                        raise noItems

                    #splitting the given input and converting it into list of string
                    input = (self.inputEntry.get()).split(sep=" ")
                        
                    # using list comprehension to  perform conversion from string list to integer list
                    inputArray = [int(i) for i in input]

                    if len(inputArray) > 15:
                        raise itemMany
                        
                    if str(self.algMenu.get()) == 'Binary Search':
                        inputArray.sort()

                    self.drawBars(inputArray, ['grey' for x in range(len(inputArray))] )

                except ValueError:
                    messagebox.showerror("Error", 
                                        "Please provide valid integer array seperated by space", parent=self.searching_win)
                    self.inputEntry.delete(0, END) 

                except itemMany:
                    messagebox.showerror("Error", 
                                        "Number of Input Entries should be less than 15", parent=self.searching_win) 
                    self.inputEntry.delete(0, END)

                except noItems:
                    messagebox.showerror("Error", 
                                "input field is mandatory",parent=self.searching_win)


            def userText(self,event):
                # print(type(self.lon))
                self.inputEntry.delete(0,END)

            def clearText(self,event):
                self.itemsearchEntry.delete(0,END)

            def back_2_home(self):
                self.searching_win.destroy()
                #import homePage



            def foundItem(itemIndex, data):
                print(itemIndex )
                result = str(data[itemIndex]) + ' found at index no: ' + str(itemIndex)
                messagebox.showinfo("Success", str(result), parent=self.searching_win)

            def drawBars(self, data, color):
                self.canvas.delete('all')
                c_width = 875
                x_width = c_width // (len(data) + 10)
                for i,height in enumerate(data):
                    x0 = 80 + (i * x_width)
                    y0 = 160
                    x1 = x0 +  x_width
                    y1 = 225

                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
                    self.canvas.create_text(x0 + 15, y0 + 40, anchor=CENTER, font = ('New Courier',13,'bold'), text=data[i])

                    
                self.searching_win.update_idletasks()


            def StartAlgorithm(self):
                global inputArray
                #int(self.inputSearch.get())
                try:
                    if self.inputEntry.get() == "sorted array seperated by space" :
                        raise noItems

                    if self.algMenu.get() == "Binary Search":
                        binarySearch(inputArray, int(self.itemsearchEntry.get()), self.drawBars, self.timeScale.get(),  self.label_index, self.label_itemfound, self.label_time)   

                    elif self.algMenu.get() == "Linear Search":

                        linearSearch(inputArray,int(self.itemsearchEntry.get()), self.drawBars, self.timeScale.get() ,  self.label_index, self.label_itemfound, self.label_time)  
                    
                except AttributeError:
                    messagebox.showerror("Error", 
                                        "item searched cannot be found in given array",parent=self.searching_win)

                except NameError:
                    messagebox.showerror("Error",
                                    "please, generate diagram for given input first.....",parent=self.searching_win)

                except ValueError:
                    messagebox.showerror("Error", 
                                        "item to be searched should be integer.....",parent=self.searching_win)
                    self.itemsearchEntry.delete(0, END)

                except noItems:
                    messagebox.showerror("Error", 
                                "all fields are mandatory to visualize algorithm",parent=self.searching_win)

        searching_win = Toplevel(self.root)
        obj = Searching(searching_win)
        searching_win.mainloop()

    def sorting_WIN(self):
        class Sorting:
            def __init__(self,sorting_win):
                self.sorting_win = sorting_win
                
                #---------window---------
                self.sorting_win.title('Algorithm Visualizer')
                self.sorting_win.geometry("900x680+200+0")
                self.sorting_win.resizable(0,0)
                self.sorting_win.config(bg='black')

                # Create style Object
                style = ttk.Style()
                style.configure('Button', font =('calibri', 20, 'bold'),borderwidth = '4')

                # Changes will be reflected
                # by the movement of mouse.
                style.map('Button', foreground = [('active', '!disabled', 'green')],
                                    background = [('active', 'black')])

                self.top_frame = Frame(self.sorting_win, width=900, height=200, bg='grey', bd=2, relief=GROOVE)
                self.top_frame.grid(row=0, column=0, padx=10, pady=5)
                self.canvas = Canvas(self.sorting_win, width=890, height=500, bg='white', bd=2, relief=SUNKEN)
                self.canvas.grid(row=1, column=0, pady=5)

                Label(self.top_frame, text='Algorithm: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=NS)
                self.algMenu = ttk.Combobox(self.top_frame ,values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
                self.algMenu.grid(row=0, column=1, padx=20, pady=5)
                self.algMenu.current(0)

                Button(self.top_frame, text='  Start   ', command=self.StartAlgorithm, background='red',  bd='4' , font = ('Callibri',10,'bold')).grid(row=0, column=3, pady=20,)

                self.timeScale = Scale(self.top_frame, from_=0.1, to=3.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
                self.timeScale.grid(padx=25, pady=5, row=0, column=2)



                Label(self.top_frame, text='Input: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=1, column=0, padx=5,  pady=5, sticky=W)
                self.inputEntry = Entry(self.top_frame, bd = '5' , relief = GROOVE,width = '30', )
                self.inputEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
                self.inputEntry.insert(0, "array seperated by space")
                self.inputEntry.bind("<Button>",self.userText)

                #Label(self.top_frame, text='Max-Size: ', bg='grey').grid(row=1, column=2, padx=15, pady=5, sticky=W)
                #inputaEntry = Entry(self.top_frame,bd = 5 , relief = GROOVE,width = 25)
                #inputaEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

                #Label for showing the execution time
                self.label_comparison = Label(self.top_frame, text=" ", bg="grey", fg="blue4",
                                                    font=("Helvetica", 12, "bold"))
                self.label_comparison.grid(row=1, column=4)

                # Entrybox for showing no of comparisons
                self.label_index = Label(self.top_frame, text="  ", bg="grey", fg="white",
                                            font=("Helvetica", 12, 'bold'))
                self.label_index.grid(row=2, column=4)

                #Entrybox for showing the number of swapped elements
                #self.label_swpindex = Label(self.top_frame, text=" ", bg="grey", fg="white",
                 #                                   font=("Helvetica", 12, "bold"))
                #self.label_swpindex.grid(row=3, column=3, pady=0)

                # button for going back to home page
                Button(self.top_frame, text='  Home   ', command=self.back_2_home, font = ('New Times Roman',11,'bold')
                                ,bg = 'sandy brown',fg = 'white', bd='2',relief=SUNKEN).grid(row=0, column=4, pady=10, padx=10)


                Button(self.top_frame, text='  Generate   ', command=self.Generate, font = ('Callibri',10,'bold'), bd='5', background='cyan' ).grid(row=1, column=2, padx=50, pady=20)


            def Generate(self):
                #self.label_comparison.destroy()
                #self.label_index.destroy()
                #self.label_swpindex.configure(text=str(0))
                self.canvas.delete('all')
                print('Algorithm selected: '+ self.algMenu.get())
                global inputArray

                try:
                    if self.inputEntry.get() == "array seperated by space":
                        raise noItems

                    #splitting the given input and converting it into list of string
                    input = (self.inputEntry.get()).split(sep=" ")
                
                    # using list comprehension to  perform conversion from string list to integer list
                    inputArray = [int(i) for i in input]

                    if len(inputArray) > 10:
                        raise itemMany

                    self.drawBars(inputArray, ['red' for x in range(len(inputArray))] )

                except ValueError:
                    messagebox.showerror("Error",
                                    "Please provide valid array seperated by space....",parent=self.sorting_win)
                    self.inputEntry.delete(0, END)

                except noItems:
                    messagebox.showerror("Error", 
                                "input field is mandatory....",parent=self.sorting_win)

                except itemMany:
                    messagebox.showerror("Error", 
                                        "Number of Input Entries should be less than or equal to 10....", parent=self.sorting_win)
                    self.inputEntry.delete(0, END)


            def userText(self,event):
            # print(type(self.lon))
                self.inputEntry.delete(0,END)

            def back_2_home(self):
                self.sorting_win.destroy()
                #import homePage

            def drawBars(self,data, color):
                self.canvas.delete('all')
                c_height = 500
                c_width = 900
                x_width = c_width /( len(data) + 4)
                offset = 30
                spacing = 40
                
                normalizedData = [i / max(data) for i in data]
                for i, height in enumerate(normalizedData):
                    x0 = i * x_width + spacing + offset
                    y0 = c_height - height * 400
                    x1 = (i + 1) * x_width + offset
                    y1 = c_height

                

                    self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
                    self.canvas.create_text(x0 + 15, y0, anchor=SW, text=str(data[i]))

                self.sorting_win.update_idletasks()

            def StartAlgorithm(self):
                global inputArray

                try:
                    #print(self.inputEntry.get())
                    if self.inputEntry.get() == "array seperated by space" :
                        raise noItems

                    if self.algMenu.get() == "Bubble Sort":
                        BubbleSort(inputArray, self.drawBars, self.timeScale.get(), self.label_comparison, self.label_index)
                        self.drawBars(inputArray, ['green' for x in range(len(inputArray))])

                    elif self.algMenu.get() == "Merge Sort":
                        merge_sort(inputArray, self.drawBars , self.timeScale.get() , self.label_comparison, self.label_index)
                        self.drawBars(inputArray, ['green' for x in range(len(inputArray))])

                    elif self.algMenu.get() == "Quick Sort":
                        QuickSort(inputArray, 0, len(inputArray)-1, self.drawBars , self.timeScale.get() , self.label_comparison, self.label_index)
                        self.drawBars(inputArray, ['green' for x in range(len(inputArray))])

                except ValueError :
                    messagebox.showerror("Error",
                                    "please, generate diagram for given input first.....",parent=self.sorting_win)

                except NameError:
                    messagebox.showerror("Error",
                                    "please, generate diagram for given input first.....",parent=self.sorting_win)

                except noItems:
                    messagebox.showerror("Error", 
                                "input field is mandatory to visualize algorithm.....",parent=self.sorting_win)

                    self.drawBars(inputArray, ['green' for x in range(len(inputArray))])
            
        sorting_win = Toplevel(self.root)
        obj = Sorting(sorting_win)
        sorting_win.mainloop()

    def loginWindow(self):
        class Login:
            def __init__(self,login_win):
                self.login_win = login_win
                self.login_win.title("Login System")
                self.login_win.geometry("900x620+100+50")
                self.login_win.resizable(False,False)

                self.bg = ImageTk.PhotoImage(file="images/login.jpg")
                self.bg_image = Label(self.login_win, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

                #=====logibn frame ====

                frame_login = Frame(self.login_win, bg="white")
                frame_login.place(x=205,y=150, height=340, width=500)

                title = Label(frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(x=130, y=30)
                
                lbl_user = Label(frame_login, text="Email", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=35, y= 105 )
                self.txt_user = Entry(frame_login, font =("times new roman",15,), bg = "lightgray")
                self.txt_user.place(x=35, y=145, width=350,height= 35)

                lbl_pass = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray", bg="white").place(x=35, y= 190 )
                self.txt_pass = Entry(frame_login, font =("times new roman",15,), bg = "lightgray")
                self.txt_pass.place(x=35, y=225, width=350,height= 35)

                register = Button(frame_login, text='Register New Account..', command=self.register_window, bg="white", fg="#d77337", bd=0, font=("times new roman", 12, )).place(x=35, y=280)
                forget = Button(frame_login, text='Forget Password?', bg="white", fg="#d77337", bd=0, font=("times new roman", 12, "underline")).place(x=210, y=280)
                login_btn = Button(self.login_win, text='Login',command=self.login_func, fg="white", bg="#d77337", font=("times new roman", 20)).place(x=350, y=470, height=40, width=180)

                btnhome = Button(self.login_win , text = 'Home' , font = ('New Times Roman',11,'bold')
                        ,bg = 'sandy brown',fg = 'white', bd='4',relief=SUNKEN, command=self.home_window)
                btnhome.place(x = 15 , y = 15)

            
            def register_window(self):
                class Register:
                    def __init__(self,reg_window):
                        self.reg_window = reg_window
                        self.reg_window.title("Registration Window")
                        self.reg_window.geometry("900x620+100+50")
                        self.reg_window.resizable(False,False)

                        self.bg = ImageTk.PhotoImage(file="images/register.jpg")
                        self.bg_image = Label(self.reg_window, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

                        #=====logibn frame ====

                        frame1 = Frame(self.reg_window, bg="white")
                        frame1.place(x=185,y=60, height=500, width=550)

                        title = Label(frame1, text="Register Here", font=("times new roman", 22, "bold"), fg="green", bg="white").place(x=50, y=20)

                        f_name = Label(frame1, text="FirstName", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=50, y=80)
                        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
                        self.txt_fname.place(x=50, y=120, width=200)

                        l_name = Label(frame1, text="LastName", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=300, y=80)
                        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
                        self.txt_lname.place(x=300, y=120, width=200)

                        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=50, y=160)
                        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
                        self.txt_email.place(x=50, y=200, width=300)

                        password = Label(frame1, text="Password", font=("times new roman", 15, "bold") , fg="gray", bg="white").place(x=50, y=240)
                        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
                        self.txt_password.place(x=50, y=280, width=200)

                        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), fg="gray", bg="white").place(x=50, y=320)
                        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
                        self.txt_cpassword.place(x=50, y=360, width=200)


                        login_redirect = Button(frame1, text='Already Have Account..', command=self.login_window,  bg="white", fg="#d77337", bd=0, font=("times new roman", 14 )).place(x=50, y=400)
                        reg_btn = Button(frame1, text="Register Now", command=self.register_data , bd=2, cursor="hand2", bg="green", fg="white",width=25, font=("times new roman", 12, "bold")).place(x=50, y=440)

                    def clear(self):
                        self.txt_fname.delete(0,END)
                        self.txt_lname.delete(0,END)
                        self.txt_email.delete(0,END)
                        self.txt_password.delete(0,END)
                        self.txt_cpassword.delete(0,END)

                    def login_window(self):
                        self.reg_window.destroy()
                    
                    
                    def register_data(self):

                        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                        if self.txt_fname.get() =="" or self.txt_lname.get() == "" or  self.txt_email.get() =="" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
                            messagebox.showerror("Error", "All Fields Are Mandatory!!", parent=self.reg_window)

                        elif not (re.search(regex,self.txt_email.get())):
                            messagebox.showerror("Error", "email format is invalid!!", parent=self.reg_window)

                        elif self.txt_password.get() != self.txt_cpassword.get() :
                            messagebox.showerror("Error", "Passwords donot match!!", parent=self.reg_window)

                        else:
                            try:
                                con = pymysql.connect(host="localhost", user="root", password="", database="algo_user")
                                cur = con.cursor()
                                cur.execute("SELECT * FROM user_info WHERE Email=%s", self.txt_email.get())
                                row = cur.fetchone()

                                if row != None:
                                    messagebox.showerror("Error", "User already exists, plz try again with another email..", parent=self.reg_window)

                                else:
                                    cur.execute("INSERT INTO user_info (FirstName, LastName, Email, Password) VALUES (%s,%s,%s,%s) ",
                                                (
                                                    self.txt_fname.get(),
                                                    self.txt_lname.get(),
                                                    self.txt_email.get(),
                                                    self.txt_password.get()
                                                ))

                                    con.commit()
                                    con.close()
                                    messagebox.showinfo("Success", "Register successful", parent=self.reg_window)
                                    self.reg_window.destroy()

                            except Exception as es:
                                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.reg_window)  

                reg_window = Toplevel(self.login_win)
                reg_obj = Register(reg_window)
                reg_window.mainloop()

            def home_window(self):
                self.login_win.destroy()
                #import dashboard

            def login_func(self):

                if self.txt_user.get() =="" or self.txt_pass.get() == "":
                    messagebox.showerror("Error", "All Fields Are Mandatory!!", parent=self.login_win)

                else:
                    try:
                        con = pymysql.connect(host="localhost", user="root", password="", database="algo_user")
                        cur = con.cursor()
                        cur.execute("SELECT * FROM user_info WHERE Email=%s AND Password=%s", (self.txt_user.get(), self.txt_pass.get()))
                        row = cur.fetchone()

                        if row==None:
                            messagebox.showerror("Error", "Invalid Username or Password!!", parent=self.login_win)

                        else:
                            print(row)
                            messagebox.showinfo("Success", "Login Successfull!!", parent=self.login_win)
                            self.home_window()
                            
                        con.close()

                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.login_win)

        login_win = Toplevel(self.root)
        obj = Login(login_win)
        login_win.mainloop()

root = Tk()
obj = HomePage(root)
root.mainloop()



