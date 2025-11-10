from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x570+225+205")


        # ===================variables====================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()  
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

         # ================= title ===========================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", borderwidth=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1300, height=50)

        # ================= logo ========================
        img1 = Image.open(r"C:\Hotel Management\Images\logohotel.png")
        img1 = img1.resize((100, 45), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1) 
        lblimg1 = Label(self.root,image=self.photoimage1, borderwidth=0)  
        lblimg1.place(x=5, y=2, width=100, height=45)

        # ================= label frame ========================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("times new roman", 12, "bold"), padx=2)   
        labelframeleft.place(x=5, y=50, width=425, height=515)  

         # ================= labels and entries ========================
        # Customer Contact
        lbl_cust_contact=Label(labelframeleft, text="Customer Contact", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W) 

        # fetch button
        btn_fetch=Button(labelframeleft,command=self.fetch_contact, text="Fetch Data", font=("times new roman", 10, "bold"), bg="black", fg="gold", width=10)
        btn_fetch.place(x=320, y=4)

        # Check In Date
        lbl_checkin=Label(labelframeleft, text="Check In Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_checkin.grid(row=1, column=0, sticky=W)

        entry_checkin=ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("times new roman", 13, "bold"))
        entry_checkin.grid(row=1, column=1)

        # Check Out Date
        lbl_checkout=Label(labelframeleft, text="Check Out Date", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_checkout.grid(row=2, column=0, sticky=W)
        entry_checkout=ttk.Entry(labelframeleft,textvariable=self.var_checkout, width=29, font=("times new roman", 13, "bold"))
        entry_checkout.grid(row=2, column=1)

        # Room Type
        lbl_roomtype=Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("times new roman", 12, "bold"), width=30, state="readonly")
        combo_roomtype["values"]=ide
        combo_roomtype.grid(row=3, column=1)
        combo_roomtype.current(0)

        # Available Room
        lbl_availableroom=Label(labelframeleft, text="Available Room", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_availableroom.grid(row=4, column=0, sticky=W)

        # txt_roomavailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29, font=("times new roman", 13, "bold"))
        # txt_roomavailable.grid(row=4, column=1)

        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("times new roman", 12, "bold"), width=30, state="readonly")
        combo_roomno["values"]=rows
        combo_roomno.grid(row=4, column=1)
        combo_roomno.current(0)




        # Meal
        lbl_meal=Label(labelframeleft, text="Meal", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)    

        txt_meal=ttk.Entry(labelframeleft,textvariable=self.var_meal, width=29, font=("times new roman", 13, "bold"))
        txt_meal.grid(row=5, column=1)

        # No of Days
        lbl_noofdays=Label(labelframeleft, text="No of Days", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_noofdays.grid(row=6, column=0, sticky=W)

        txt_noofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29, font=("times new roman", 13, "bold"))
        txt_noofdays.grid(row=6, column=1)

        # Paid Tax
        lbl_paidtax=Label(labelframeleft, text="Paid Tax", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_paidtax.grid(row=7, column=0, sticky=W)

        txt_paidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=("times new roman", 13, "bold"))
        txt_paidtax.grid(row=7, column=1)

        # Sub Total
        lbl_subtotal=Label(labelframeleft, text="Sub Total", font=("times new roman", 12, "bold"), padx=2, pady=6)  
        lbl_subtotal.grid(row=8, column=0, sticky=W)    

        txt_subtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29, font=("times new roman", 13, "bold"))
        txt_subtotal.grid(row=8, column=1)

        # Total Cost
        lbl_totalcost=Label(labelframeleft, text="Total Cost", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_totalcost.grid(row=9, column=0, sticky=W)   

        txt_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total, width=29, font=("times new roman", 13, "bold"))
        txt_totalcost.grid(row=9, column=1)

        # Bill Button
        bill_btn = Button(labelframeleft,command=self.total, text="BILL",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        bill_btn.grid(row=10, column=0,sticky=W)

         # ================== buttons ========================
        btn_frame = Frame(labelframeleft, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        add_btn = Button(btn_frame,command=self.add_data, text="ADD",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        add_btn.grid(row=0, column=0, padx=1,pady=1)

        update_btn = Button(btn_frame,command=self.update_data, text="UPDATE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        update_btn.grid(row=0, column=1, padx=1,pady=1 )

        delete_btn = Button(btn_frame,command=self.delete_data, text="DELETE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        delete_btn.grid(row=0, column=2, padx=1,pady=1 )    

        reset_btn = Button(btn_frame,command=self.reset_data, text="RESET",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        reset_btn.grid(row=0, column=3, padx=1,pady=1  )

        # ================= Right side image ========================
        img3 = Image.open(r"C:\Hotel Management\Images\bed.jpg")
        img3 = img3.resize((530, 300), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3) 
        lblimg3 = Label(self.root,image=self.photoimage3, bd=0,relief=RIDGE)  
        lblimg3.place(x=760, y=55, width=530, height=300)


         # ================== table frame ========================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)   
        table_frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy=Label(table_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")    
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var, font=("times new roman", 12, "bold"), width=24, state="readonly")
        combo_search["values"]=("Contact", "Room")
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
        details_table.place(x=0, y=50, width=855, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")    
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")  
        

        self.room_table['show']='headings'

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=150)  
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
             messagebox.showerror("Error", "All Fields are required", parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(), 
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()
                                                                                        ))
                messagebox.showinfo("Success", "Room has been booked successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                    self.room_table.insert("", END, values=i)
             conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),      
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    # update
    def update_data(self):
        if self.var_contact.get()=="":
             messagebox.showerror("Error", "Please enter mobile number", parent=self.root) 
        else:
               
                    conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, room=%s, meal=%s, noofdays=%s where Contact=%s",(
                        
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(), 
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get(),
                                                                                                    self.var_contact.get()
                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Room details has been updated successfully", parent=self.root)

    # delete
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System", "Do you want to delete this room booking?", parent=self.root)
        if delete_data > 0:
              conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
              my_cursor = conn.cursor()
              query = "delete from room where Contact=%s"
              value = (self.var_contact.get(),)
              my_cursor.execute(query, value)
        else:
            if not delete_data:
                     return 
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset data
    def reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),      
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),   
        self.var_total.set("")
     

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)

        else:
            conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblname = Label(showDataframe, text="Name : ", font=("times new roman", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl=Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl.place(x=90, y=0)

                # gender
                conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)   
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataframe, text="Gender : ", font=("times new roman", 12, "bold"))
                lblgender.place(x=0, y=30)
                lbl2=Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl2.place(x=90, y=30)

                # email
                conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")  
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")  
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text="Email : ", font=("times new roman", 12, "bold"))
                lblemail.place(x=0, y=60)
                lbl3=Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl3.place(x=90, y=60)

                # nationality
                conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value) 

                row = my_cursor.fetchone()  

                lblnationality = Label(showDataframe, text="Nationality : ", font=("times new roman", 12, "bold"))
                lblnationality.place(x=0, y=90)

                lbl4=Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl4.place(x=90, y=90)

                # address
                conn = mysql.connector.connect(host="localhost", username="root", database="hotel_management")  
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")    
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text="Address : ", font=("times new roman", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbl5=Label(showDataframe, text=row, font=("times new roman", 12, "bold"))
                lbl5.place(x=90, y=120)

    # search data
    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                 self.room_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()

        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs((outDate-inDate).days))

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%(q5*0.1))
            totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
            self.var_total.set(totalcost)

        
        elif   (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
                q1=float(300)
                q2=float(800)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
                q1=float(300)
                q2=float(1000)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                q1=float(400)
                q2=float(600)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
                q1=float(400)
                q2=float(800)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
                q1=float(400)
                q2=float(1000)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                q1=float(500)
                q2=float(600)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                q1=float(500)
                q2=float(800)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        elif   (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                q1=float(500)
                q2=float(1000)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3*q4)
                tax="Rs."+str("%.2f"%(q5*0.1))
                totalcost="Rs."+str("%.2f"%(q5+ (q5*0.1)))

                self.var_paidtax.set(tax)
                self.var_actualtotal.set("Rs."+str("%.2f"%(q5)))
                self.var_total.set(totalcost)

        else:
             messagebox.showerror('warning','Something wrong here...')
        




if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()