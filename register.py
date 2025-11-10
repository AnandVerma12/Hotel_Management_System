from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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
        self.bg = ImageTk.PhotoImage(file=r"C:\Hotel Management\Images\blue-surface-with-study-tools.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    

        # =============== left image ==================
        img1 = Image.open(r"C:\Hotel Management\Images\2838014.jpg")
        img1 = img1.resize((400, 500), Image.Resampling.LANCZOS) 
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, borderwidth=0)  
        lblimg1.place(x=120, y=150, width=400, height=500)

        # ============== main frame ==================
        frame = Frame(self.root, bg="skyblue")
        frame.place(x=520, y=150, width=800, height=500)    

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

        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), fg="white", bg="blue", activeforeground="white", activebackground="blue", cursor="hand2")
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





        



if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()     