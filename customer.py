from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x570+225+205")

        # ================ variables ==================

        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar() 
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()


        # ================= title ===========================
        lbl_title = Label(self.root, text=" ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", borderwidth=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # ================= logo ========================
        img1 = Image.open(r"C:\Hotel Management\Images\logohotel.png")
        img1 = img1.resize((100, 45), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1) 
        lblimg1 = Label(self.root,image=self.photoimage1, borderwidth=0)  
        lblimg1.place(x=5, y=2, width=100, height=45)

        # ================= label frame ========================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)   
        labelframeleft.place(x=5, y=50, width=425, height=515)  

        # ================= labels and entries ========================
        # cust_ref
        lbl_cust_ref=Label(labelframeleft, text="Customer Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, width=29, font=("times new roman", 13, "bold"),state="readonly")
        entry_ref.grid(row=0, column=1) 

        # cust name
        lbl_cust_name=Label(labelframeleft, text="Customer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)

        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_name, width=29, font=("times new roman", 13, "bold"))
        entry_name.grid(row=1, column=1)    

        # mother name
        lbl_mother_name=Label(labelframeleft, text="Mother Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mother_name.grid(row=2, column=0, sticky=W)

        entry_mother=ttk.Entry(labelframeleft,textvariable=self.var_mother, width=29, font=("times new roman", 13, "bold"))
        entry_mother.grid(row=2, column=1)  

        # gender
        lbl_gender=Label(labelframeleft, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=30, state="readonly")
        combo_gender["values"]=("Male", "Female", "Other")  
        combo_gender.grid(row=3, column=1)  
        combo_gender.current(0) 
        
        # post code
        lbl_post_code=Label(labelframeleft, text="Post Code", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_post_code.grid(row=4, column=0, sticky=W)   

        entry_post_code=ttk.Entry(labelframeleft,textvariable=self.var_post, width=29, font=("times new roman", 13, "bold"))
        entry_post_code.grid(row=4, column=1)   

        # mobile
        lbl_mobile=Label(labelframeleft, text="Mobile", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)

        entry_mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("times new roman", 13, "bold"))
        entry_mobile.grid(row=5, column=1)

        # email
        lbl_email=Label(labelframeleft, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)

        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_email.grid(row=6, column=1)

        # nationality
        lbl_nationality=Label(labelframeleft, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W) 

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("times new roman", 12, "bold"), width=30, state="readonly")
        combo_nationality["values"]=("Indian", "American", "British", "Other")      
        combo_nationality.grid(row=7, column=1) 
        combo_nationality.current(0)

        # id proof
        lbl_id_proof=Label(labelframeleft, text="ID Proof", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_id_proof.grid(row=8, column=0, sticky=W)
    
        combo_id_proof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof, font=("times new roman", 12, "bold"), width=30, state="readonly")
        combo_id_proof["values"]=("Aadhar Card", "Driving License", "Passport", "Voter ID")      
        combo_id_proof.grid(row=8, column=1)    
        combo_id_proof.current(0)


        # id number
        lbl_id_number=Label(labelframeleft, text="ID Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)

        entry_id_number=ttk.Entry(labelframeleft,textvariable=self.var_idnumber, width=29, font=("times new roman", 13, "bold"))
        entry_id_number.grid(row=9, column=1)

        # address
        lbl_address=Label(labelframeleft, text="Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_address, width=29, font=("times new roman", 13, "bold"))
        entry_address.grid(row=10, column=1)

        # ================== buttons ========================
        btn_frame = Frame(labelframeleft, relief=RIDGE)
        btn_frame.place(x=10, y=400, width=412, height=40)

        add_btn = Button(btn_frame,command=self.add_data, text="ADD",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        add_btn.grid(row=0, column=0, padx=1,pady=1)

        update_btn = Button(btn_frame,command=self.update_data, text="UPDATE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        update_btn.grid(row=0, column=1, padx=1,pady=1 )

        delete_btn = Button(btn_frame,command=self.delete_data, text="DELETE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        delete_btn.grid(row=0, column=2, padx=1,pady=1 )    

        reset_btn = Button(btn_frame,command=self.reset_data, text="RESET",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        reset_btn.grid(row=0, column=3, padx=1,pady=1  )

        # ================== table frame ========================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)   
        table_frame.place(x=435, y=50, width=860, height=515)

        lblSearchBy=Label(table_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")    
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["values"]=("Mobile", "Ref")
        combo_search.grid(row=0, column=1, padx=2)
        combo_search.current(0)


        self.search_txt=StringVar()
        entry_search=ttk.Entry(table_frame,textvariable=self.search_txt, width=24, font=("times new roman", 13, "bold"))
        entry_search.grid(row=0, column=2, padx=2)  

        search_btn = Button(table_frame,command=self.search, text="SEARCH",  width=11, font=("times new roman", 11, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        search_btn.grid(row=0, column=3, padx=1)    

        showall_btn = Button(table_frame,command=self.fetch_data, text="SHOW ALL",  width=11, font=("times new roman", 11, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        showall_btn.grid(row=0, column=4, padx=1)   

        # ==================show data table ========================

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=855, height=400)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_table = ttk.Treeview(details_table, columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_table.xview)
        scroll_y.config(command=self.cust_table.yview)

        self.cust_table.heading("ref", text="Ref No")
        self.cust_table.heading("name", text="Name")    
        self.cust_table.heading("mother", text="Mother Name")
        self.cust_table.heading("gender", text="Gender")
        self.cust_table.heading("post", text="Post Code")
        self.cust_table.heading("mobile", text="Mobile")
        self.cust_table.heading("email", text="Email")  
        self.cust_table.heading("nationality", text="Nationality")
        self.cust_table.heading("idproof", text="ID Proof")
        self.cust_table.heading("idnumber", text="ID Number")
        self.cust_table.heading("address", text="Address")

        self.cust_table['show']='headings'

        self.cust_table.column("ref", width=100)
        self.cust_table.column("name", width=100)
        self.cust_table.column("mother", width=100)
        self.cust_table.column("gender", width=100)
        self.cust_table.column("post", width=100)
        self.cust_table.column("mobile", width=100)
        self.cust_table.column("email", width=150)  
        self.cust_table.column("nationality", width=100)
        self.cust_table.column("idproof", width=100)    
        self.cust_table.column("idnumber", width=100)
        self.cust_table.column("address", width=150)    

        self.cust_table.pack(fill=BOTH, expand=1)
        self.cust_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
             messagebox.showerror("Error", "All Fields are required", parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                    self.var_ref.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_idproof.get(),
                                                                                                    self.var_idnumber.get(),
                                                                                                    self.var_address.get(),
                                                                                                    ))
                messagebox.showinfo("Success", "Customer has been added successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)
             
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
             self.cust_table.delete(*self.cust_table.get_children())
             for i in rows:
                    self.cust_table.insert("", END, values=i)
             conn.commit()
        conn.close()
         

    def get_cursor(self, event=""):
        cursor_row = self.cust_table.focus()
        content = self.cust_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),      
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]), 
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),       
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get()=="":
             messagebox.showerror("Error", "Please enter mobile number", parent=self.root) 
        else:
               
                    conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IDProof=%s, IDNumber=%s, Address=%s where Ref=%s",(
                        
                                                                                                    self.var_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_idproof.get(),
                                                                                                    self.var_idnumber.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_ref.get(),
                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Customer details has been updated successfully", parent=self.root)
           
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if delete_data > 0:
              conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
              my_cursor = conn.cursor()
              query = "delete from customer where Ref=%s"
              value = (self.var_ref.get(),)
              my_cursor.execute(query, value)
        else:
            if not delete_data:
                     return 
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        #   self.var_ref.set(row[0]),
        self.var_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),      
        self.var_mobile.set(""),
        self.var_email.set(""), 
        # self.var_nationality.set(""),
        # self.var_idproof.set(""),       
        self.var_idnumber.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

         
    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where " + str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                 self.cust_table.insert("", END,values=i)
            conn.commit()
        conn.close()
        
            



    


                    




if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()