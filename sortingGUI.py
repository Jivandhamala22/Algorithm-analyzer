from ctypes import sizeof
from os import sep
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from pymysql import NULL
from Exceptions import *
from sortingAlgorithms import BubbleSort, merge_sort, QuickSort

class Sorting:
    def __init__(self,root):
        self.root = root
        
        #---------window---------
        self.root.title('Sorting System')
        self.root.geometry("900x620+250+30")
        self.root.resizable(0,0)
        self.root.config(bg='black')

        # Create style Object
        style = ttk.Style()
        style.configure('Button', font =('calibri', 20, 'bold'),borderwidth = '4')

        # Changes will be reflected
        # by the movement of mouse.
        style.map('Button', foreground = [('active', '!disabled', 'green')],
                            background = [('active', 'black')])

        self.top_frame = Frame(self.root, width=900, height=200, bg='grey')
        self.top_frame.grid(row=0, column=0, padx=10, pady=5)
        self.canvas = Canvas(self.root, width=900, height=470, bg='white')
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

        Label(self.top_frame, text='Algorithm: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=0, column=0, padx=5, pady=5, sticky=NS)
        self.algMenu = ttk.Combobox(self.top_frame ,values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
        self.algMenu.grid(row=0, column=1, padx=20, pady=5)
        self.algMenu.current(0)

        Button(self.top_frame, text='  Start   ', command=self.StartAlgorithm, background='red',  bd='4' , font = ('Callibri',10,'bold')).grid(row=0, column=3, padx=20, pady=20)

        self.timeScale = Scale(self.top_frame, from_=0.1, to=3.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
        self.timeScale.grid(padx=15, pady=5, row=0, column=2)



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
        self.label_comparison.grid(row=1, column=3)

        # Entrybox for showing no of comparisons
        self.label_index = Label(self.top_frame, text="  ", bg="grey", fg="white",
                                    font=("Helvetica", 15, 'bold'))
        self.label_index.grid(row=2, column=3)

        #Entrybox for showing the number of swapped elements
        self.label_swpindex = Label(self.top_frame, text="  ", bg="grey", fg="white",
                                            font=("Helvetica", 15, "bold"))
        self.label_swpindex.grid(row=3, column=3, pady=0)

        # button for going back to home page
        Button(self.top_frame, text='  Home   ', command=self.back_2_home, font = ('New Times Roman',11,'bold')
                        ,bg = 'sandy brown',fg = 'white', bd='2',relief=SUNKEN).place(x=720,y=20)


        Button(self.top_frame, text='  Generate   ', command=self.Generate, font = ('Callibri',10,'bold'), bd='5', background='cyan' ).grid(row=1, column=2, padx=50, pady=10)


    def Generate(self):
        self.canvas.delete('all')
        print('Algorithm selected: '+ self.algMenu.get())
        global inputArray

        try:
        
            if self.inputEntry.get() == "array seperated by space"  :
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
                            "Please provide valid array seperated by space....",parent=self.root)
            self.inputEntry.delete(0, END)

        except itemMany:
                    messagebox.showerror("Error", 
                                        "Number of Input Entries should be less than 10....", parent=self.root)
                    self.inputEntry.delete(0, END)

        except noItems:
            messagebox.showerror("Error", 
                                "input field is mandatory....",parent=self.root)


    def userText(self,event):
    # print(type(self.lon))
        self.inputEntry.delete(0,END)

    def back_2_home(self):
        self.root.destroy()
        #import homePage

    def drawBars(self,data, color):
        self.canvas.delete('all')
        c_height = 470
        c_width = 900
        x_width = c_width /( len(data) + 4)
        offset = 30
        spacing = 40
        
        normalizedData = [(i) / max(data) for i in data]
        for i, height in enumerate(normalizedData):
            x0 = i * x_width + spacing + offset
            y0 = c_height - height * 400
            x1 = (i + 1) * x_width + offset
            y1 = c_height     

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
            self.canvas.create_text(x0 + 15, y0, anchor=SW, text=str(data[i]))

        self.root.update_idletasks()

    def StartAlgorithm(self):
        global inputArray

        try:
            #print(inputArray)
            if self.inputEntry.get() == "array seperated by space" :
                raise noItems

            if self.algMenu.get() == "Bubble Sort":
                BubbleSort(inputArray, self.drawBars, self.timeScale.get(), self.label_comparison, self.label_index, self.label_swpindex)
                self.drawBars(inputArray, ['green' for x in range(len(inputArray))])

            elif self.algMenu.get() == "Merge Sort":
                merge_sort(inputArray, self.drawBars , self.timeScale.get() ,self.label_comparison,  self.label_index)
                self.drawBars(inputArray, ['green' for x in range(len(inputArray))])

            elif self.algMenu.get() == "Quick Sort":
                QuickSort(inputArray, 0, len(inputArray)-1, self.drawBars , self.timeScale.get() , self.label_comparison, self.label_index)
                self.drawBars(inputArray, ['green' for x in range(len(inputArray))])
        
        #except AttributeError:
          #  messagebox.showerror("Error",
            #                "please, generate diagram for given input first.....",parent=self.root)
          #  self.inputEntry.delete(0, END)

        except ValueError:
            messagebox.showerror("Error",
                            "please, generate diagram for given input first.....",parent=self.root)

        except noItems:
            messagebox.showerror("Error", 
                                "input field is mandatory to visualize algorithm",parent=self.root)

        #finally:
           # self.drawBars(inputArray, ['green' for x in range(len(inputArray))])
    
root = Tk()
obj = Sorting(root)
root.mainloop()
