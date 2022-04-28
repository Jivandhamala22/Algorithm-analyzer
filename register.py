from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
import pymysql
import re

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("900x620+100+50")
        self.root.resizable(False,False)

        self.bg = ImageTk.PhotoImage(file="images/register.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)

        #=====logibn frame ====

        frame1 = Frame(self.root, bg="white")
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


        register = Button(frame1, text='Already Have Account..', command=self.login_window,  bg="white", fg="#d77337", bd=0, font=("times new roman", 14, )).place(x=50, y=400)
        reg_btn = Button(frame1, text="Register Now", command=self.register_data , bd=2, cursor="hand2", bg="green", fg="white",width=25, font=("times new roman", 12, "bold")).place(x=50, y=440)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)

    def login_window(self):
        self.root.destroy()
        import login
    
    def register_data(self):

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if self.txt_fname.get() =="" or self.txt_lname.get() == "" or  self.txt_email.get() =="" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields Are Mandatory!!", parent=self.root)

        elif not (self.txt_fname.get().isalpha() or self.txt_lname.get().isalpha()):
            messagebox.showerror("Error", "provide valid firstname and lastname!!", parent=self.root)

        elif not(len(self.txt_fname.get()) > 5 or len(self.txt_lname.get()) > 5):
            messagebox.showerror("Error", "minimum length for first and last name is 5 !!!", parent=self.root)

        elif not (re.search(regex,self.txt_email.get())):
            messagebox.showerror("Error", "email format is invalid!!", parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get() :
            messagebox.showerror("Error", "Passwords donot match!!", parent=self.root)

        else:

            try:

                con = pymysql.connect(host="localhost", user="root", password="", database="algo_user")
                cur = con.cursor()
                cur.execute("SELECT * FROM user_info WHERE Email=%s", self.txt_email.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User already exists, plz try again with another email..", parent=self.root)

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
                    messagebox.showinfo("Success", "Register successful", parent=self.root)
                    self.root.destroy()
                    import login


            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)
       
root = Tk()
obj = Register(root)
root.mainloop()