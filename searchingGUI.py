from os import sep
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from searchingAlgorithm import binarySearch, linearSearch
from Exceptions import *

class Searching:
    def __init__(self,root):
        self.root = root
        #----------window---------
        self.root.title('Searching System')
        self.root.geometry("900x620+250+30")
        self.root.resizable(0,0)
        self.root.config(bg='black')

        self.top_frame = Frame(self.root, width=900, height=200, bg='grey')
        self.top_frame.grid(row=0, column=0, padx=10, pady=5)
        self.canvas = Canvas(self.root, width=875, height=450, bg='white')
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

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
        print(self.algMenu.get())
        global inputArray

        try:
            if self.inputEntry.get() == "sorted array seperated by space"  :
                raise noItems
            #splitting the given input and converting it into list of string
            input = (self.inputEntry.get()).split(sep=" ")
                
            # using list comprehension to  perform conversion from string list to integer list
            inputArray = [int(i) for i in input]

            if len(inputArray) > 12:
                raise itemMany 
            if str(self.algMenu.get()) == 'Binary Search':
                inputArray.sort()

            self.drawBars(inputArray, ['grey' for x in range(len(inputArray))] )

        except ValueError:
            messagebox.showerror("Error", 
                                "Please provide valid integer array seperated by space", parent=self.root)
            self.inputEntry.delete(0, END)  

        except itemMany:
                    messagebox.showerror("Error", 
                                        "Number of Input Entries should be less than 12", parent=self.root)
                    self.inputEntry.delete(0, END) 

        except noItems:
            messagebox.showerror("Error", 
                                "input field is mandatory",parent=self.root)


    def userText(self,event):
        # print(type(self.lon))
        self.inputEntry.delete(0,END)

    def clearText(self,event):
        self.itemsearchEntry.delete(0,END)

    def back_2_home(self):
        self.root.destroy()
        #import homePage



    def foundItem(itemIndex, data):
        print(itemIndex )
        result = str(data[itemIndex]) + ' found at index no: ' + str(itemIndex)
        messagebox.showinfo("Success", str(result))

    def drawBars(self, data, color):
        self.canvas.delete('all')
        c_width = 875
        x_width = c_width // (len(data) + 10)
        for i,height in enumerate(data):
            x0 = 80 + (i * x_width)
            y0 = 160
            x1 = x0 +  x_width
            y1 = 225

            self.canvas.create_rectangle(x0, y0, x1+25, y1, fill=color[i])
            self.canvas.create_text(x0 + 25, y0 + 40, anchor=CENTER, font = ('New Courier',13,'bold'), text=data[i])

            
        self.root.update_idletasks()


    def StartAlgorithm(self):
        global inputArray
        print(self.inputEntry.get())
        
        try:
            inputSearch = int(self.itemsearchEntry.get())

            if self.inputEntry.get() == "sorted array seperated by space" :
                raise noItems

            if self.algMenu.get() == "Binary Search":
                binarySearch(inputArray, inputSearch, self.drawBars, self.timeScale.get(),  self.label_index, self.label_itemfound,self.label_time)   

            elif self.algMenu.get() == "Linear Search":
                linearSearch(inputArray, inputSearch, self.drawBars, self.timeScale.get() ,  self.label_index, self.label_itemfound, self.label_time)  
                

        except noItems:
            messagebox.showerror("Error", 
                                "all fields are mandatory....",parent=self.root)

        except searchEntryBlank:
            messagebox.showerror("Error", 
                                "search field is blank....",parent=self.root)
        
        except ValueError:
            messagebox.showerror("Error", 
                                "please, generate diagram for given input first....",parent=self.root)
            self.itemsearchEntry.delete(0, END)


root = Tk()
obj = Searching(root)
root.mainloop()