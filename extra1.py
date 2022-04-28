from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from os import sep
from tkinter import messagebox
import pymysql,re

import random

root = Tk()

root.title("Job Processing Window")
root.geometry("1050x670+130+0")
root.resizable(False,False)
root.config(bg='gray')

frame1 = Frame(root, width=1050, height=150, bg='gray', bd = 5, relief = SUNKEN )
frame1.pack()
frame2 = Frame(root, width=1050, height=590, bg='white', bd = 2 , relief = SUNKEN)
frame2.pack()

Label(frame1, text='Algorithm: ', bg='grey', font = ('Helvetica',12,'bold')).grid(row=0, column=0,
                 padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(frame1,values=['FCFS', 'Round Robin'])
algMenu.grid(row=0, column=1, pady=5)
algMenu.current(0)

timeScale = Scale(frame1, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, 
        orient=HORIZONTAL, label="Select Speed [s]")
timeScale.grid(padx=15, pady=5, row=0, column=2)

Label(frame1, text='Arrival Time* ', font = ('Helvetica',12,'bold')).place(x=100, y=70)
arrivaltime = Entry(frame1, font=("times new roman", 15), bg="lightgray")
arrivaltime.place(x=200, y=70, width=100)

 # button for going back to home page
Button(frame1, text='  HOME   ', command='', font = ('New Times Roman',11,'bold')
        ,bg = 'sandy brown',fg = 'white', bd='2',relief=SUNKEN).grid(row=0, column=4, padx=20, pady=10)

# button for start algorithm
Button(frame1, text='  START   ', command='', font = ('New Times Roman',11,'bold')
        ,bg = 'red',fg = 'white', bd='2',relief=SUNKEN).grid(row=0, column=3, padx=20, pady=10)

#labelframe for input data table
frame3 = LabelFrame(frame2, width = 400, height=250, bg = 'white',bd=0, font=("New Times Roman", 
                        12, 'bold'),  text='Input Data', pady=10)
frame3.place(x=10, y=20)

#scrollbar for input data table
tree_scroll = Scrollbar(frame3)
tree_scroll.pack(side=RIGHT, fill=Y)

# Table formation using TreeView method
my_tree = ttk.Treeview(frame3, yscrollcommand = tree_scroll.set)
my_tree['show'] = 'headings'

# style for table
s = ttk.Style(frame3)
s.theme_use("clam")
s.configure(".", font=("Helvetica", 11))
s.configure("Treeview.Heading", foreground='red', font=("Helvetica", 12, 'bold'))

#configure scrollbar
tree_scroll.config(command=my_tree.yview)

#defining no of columns of the table
my_tree["columns"] = ("Process Id", "Arrival Time", "Burst Time", "Priority")
#assigning properties of each column
my_tree.column("Process Id", anchor=CENTER, width=100)
my_tree.column("Arrival Time", anchor=CENTER, width=100)
my_tree.column("Burst Time", anchor=CENTER, width=100)
my_tree.column("Priority", anchor=CENTER, width=100)

#assigning heading names to each column
my_tree.heading("Process Id", text="Process Id", anchor=CENTER)
my_tree.heading("Arrival Time",text="Arrival Time", anchor=CENTER)
my_tree.heading("Burst Time",text="Burst Time", anchor=CENTER)
my_tree.heading("Priority", text="Priority",anchor=CENTER)

my_tree.pack()

#labelframe for job pool
frame4 = LabelFrame(frame2, width = 610, height=400, bg = 'white',bd=5, font=("New Times Roman", 
                        12, 'bold'),  text='Process Pool', pady=10)
frame4.place(x=430, y=20)

#scrollbar for job pool
jobpooltree_scroll = Scrollbar(frame4)
jobpooltree_scroll.pack(side=RIGHT, fill=Y)

# Table formation using TreeView method
jobpool_tree = ttk.Treeview(frame4, yscrollcommand = jobpooltree_scroll.set )
jobpool_tree['show'] = 'headings'

# style for table
s = ttk.Style(frame4)
s.theme_use("clam")
s.configure(".", font=("Helvetica", 10))
s.configure("Treeview.Heading", foreground='black', font=("Helvetica", 10, 'bold'))

#configure scrollbar
jobpooltree_scroll.config(command=jobpool_tree.yview)

#defining no of columns of the table
jobpool_tree["columns"] = ("Process", "Status Bar", "Remaining Burst Time", "Waiting Time")
#assigning properties of each column
jobpool_tree.column("Process", anchor=CENTER, width=70)
jobpool_tree.column("Status Bar", anchor=CENTER, width=270)
jobpool_tree.column("Remaining Burst Time", anchor=CENTER, width=150, stretch=YES)
jobpool_tree.column("Waiting Time", anchor=CENTER, width=100)

#assigning heading names to each column
jobpool_tree.heading("Process", text="Process", anchor=CENTER)
jobpool_tree.heading("Status Bar",text="Status Bar", anchor=CENTER)
jobpool_tree.heading("Remaining Burst Time",text="Remaining Burst Time", anchor=CENTER)
jobpool_tree.heading("Waiting Time", text="Waiting Time",anchor=CENTER)

jobpool_tree.pack()

#labelframe for ready queue
frame5 = LabelFrame(frame2, width = 400, height=90, bg = 'white',bd=1, font=("New Times Roman", 
                        12, 'bold'),  text='Ready Queue', pady=10)
frame5.place(x=10, y=295)

#labelframe for current job in cpu
frame6 = LabelFrame(frame2, width = 400, height=80, bg = 'white',bd=1, font=("New Times Roman", 
                        12, 'bold'),  text='CPU', pady=10)
frame6.place(x=10, y=395)

#labelframe for gantt chart
frame7 = LabelFrame(frame2, width = 800, height=80, bg = 'white',bd=2, font=("New Times Roman", 
                        12, 'bold'),  text='Gantt Chart', pady=10)
frame7.place(x=10, y=495)


root.mainloop()