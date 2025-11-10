from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
    win =Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        
        

        self.bg = ImageTk.PhotoImage(file=r"C:\Hotel Management\Images\bg.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=350, height=450)

        img1 = Image.open(r"C:\Hotel Management\Images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS) 
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)  
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        self.var_email=StringVar()
        username=lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")    
        username.place(x=70, y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        self.var_pass=StringVar()
        password=lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")    
        password.place(x=70, y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)  

        
        # icon images
        img2 = Image.open(r"C:\Hotel Management\Images\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS) 
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)  
        lblimg2.place(x=650, y=324, width=25, height=25)

        img3 = Image.open(r"C:\Hotel Management\Images\lock-512.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS) 
        self.photoimage3 = ImageTk.PhotoImage(img3)     
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)  
        lblimg3.place(x=650, y=395, width=25, height=25)

        # login button
        loginbtn=Button(frame,command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # register button
        registerbtn=Button(frame,command=self.register_window, text="New User Register", font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forgot password button
        forgotbtn=Button(frame,command=self.forgot_password, text="Forgot Password", font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")   
        forgotbtn.place(x=15, y=375, width=160)
    
    # register window
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


        # login system
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get()=="anand" and self.txtpass.get()=="1210":
            messagebox.showinfo("Success", "Welcome to Hotel Management System")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")
            my_cursor = conn.cursor()       
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                     ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)   
                else:
                    if not open_main:
                        return  
            conn.commit()
            conn.close()
            
# ============================= Reset password ==============================
    def reset_password(self):
        if self.combo_security_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:   
            conn=mysql.connector.connect(host="localhost", username="root", database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()    
            if row==None:
                messagebox.showerror("Error", "Please enter the correct answer")
            else:   
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with new password")
                self.forget_win.destroy()
                

# ============================== forgot password ==============================
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset your password")  
        else:   
            conn=mysql.connector.connect(host="localhost", username="root", database="hotel_management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()    
            if row==None:
                messagebox.showerror("Error", "Please enter the valid username")
            else:   
                conn.close()
                # ====== reset password window ======
                self.forget_win=Toplevel(self.root)
                self.forget_win.title("Reset Password")
                self.forget_win.geometry("400x400+500+100")

                l=Label(self.forget_win, text="Reset Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                self.security_Q=Label(self.forget_win, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")    
                self.security_Q.place(x=50, y=80)    

                self.combo_security_Q=ttk.Combobox(self.forget_win, font=("times new roman", 13, "bold"), state="readonly")
                self.combo_security_Q['values']=("Select", "Your Birth Place", "Your Pet")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50, y=110, width=250)  

                self.security_A=Label(self.forget_win, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
                self.security_A.place(x=50, y=150)

                self.txt_security=ttk.Entry(self.forget_win, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                self.new_password=Label(self.forget_win, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
                self.new_password.place(x=50, y=220) 

                self.txt_new_password=ttk.Entry(self.forget_win, font=("times new roman", 15, "bold"))
                self.txt_new_password.place(x=50, y=250, width=250)  

                btn=Button(self.forget_win, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green", activeforeground="white", activebackground="green", cursor="hand2", command=self.reset_password)
                btn.place(x=150, y=300, width=100)



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1350x700+0+0")

        # ================== Variables ======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        # bg image
        self.bg = ImageTk.PhotoImage(file=r"C:\Hotel Management\Images\3053475.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        

        # # =============== left image ==================
        # img4 = Image.open(r"C:\Hotel Management\Images\2838014.jpg")
        # img4 = img4.resize((400, 500), Image.Resampling.LANCZOS) 
        # self.photoimage4 = ImageTk.PhotoImage(img4)
        # lblimg4 = Label(image=self.photoimage4, borderwidth=0)  
        # lblimg4.place(x=120, y=150, width=400, height=500)

        # ============== main frame ==================
        frame = Frame(self.root, bg="skyblue")
        frame.place(x=520, y=150, width=800, height=500)  

        self.bg1 = ImageTk.PhotoImage(file=r"C:\Hotel Management\Images\43916.jpg")
        bg_label2 = Label(self.root, image=self.bg1)
        bg_label2.place(x=120, y=150, width=400, height=500)  

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="skyblue")
        register_lbl.place(x=20, y=20)  

        # ============== labels and entries ==================

        # ---------------Row1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        fname.place(x=50, y=100)
        self.txt_fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.txt_fname.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # --------------Row2

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        contact.place(x=50, y=170)  
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        email.place(x=370, y=170)   

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)   

        # ---------------Row3

        security_Q = Label(frame, text="Security Question", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 13, "bold"), state="readonly")
        self.combo_security_Q['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        security_A.place(x=370, y=240)  
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # -----------------Row4

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        password.place(x=50, y=310) 
        self.txt_password = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        self.txt_password.place(x=50, y=340, width=250) 

        confirm_pwd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="skyblue")    
        confirm_pwd.place(x=370, y=310) 
        self.txt_confirm_pwd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"), show="*")
        self.txt_confirm_pwd.place(x=370, y=340, width=250)

        # =============== check button ==================
        check_btn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), bg="skyblue", onvalue=1, offvalue=0)
        check_btn.place(x=50, y=380)

        # =============== register button ==================
        register_btn = Button(frame, text="Register Now", font=("times new roman", 15, "bold"), fg="white", bg="green", activeforeground="white", activebackground="green", cursor="hand2",command=self.regsiter_data)
        register_btn.place(x=50, y=420, width=200, height=40)

        login_btn = Button(frame,command=self.return_login, text="Login", font=("times new roman", 15, "bold"), fg="white", bg="blue", activeforeground="white", activebackground="blue", cursor="hand2")
        login_btn.place(x=370, y=420, width=150, height=40)

        

    
    # ================ Function Declaration ====================

    def regsiter_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try with another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.var_fname.get(),
                                                                self.var_lname.get(),
                                                                self.var_contact.get(),
                                                                self.var_email.get(),
                                                                self.var_securityQ.get(),
                                                                self.var_securityA.get(),
                                                                self.var_pass.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successful")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
