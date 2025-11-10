from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class RoomDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x570+225+205")

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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Add New Room", font=("times new roman", 12, "bold"), padx=2)   
        labelframeleft.place(x=5, y=50, width=540, height=350) 

        # ================ labels and entries ===================== 

        # Floor
        lbl_floor=Label(labelframeleft, text="Floor", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor, width=20, font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0, column=1,sticky=W) 

        # Room No
        lbl_roomno=Label(labelframeleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomno.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno, width=20, font=("times new roman", 13, "bold"))
        entry_roomno.grid(row=1, column=1,sticky=W)

        # Room Type
        lbl_roomtype=Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)

        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype, width=20, font=("times new roman", 13, "bold"))  
        entry_roomtype.grid(row=2, column=1,sticky=W)

         # ================== buttons ========================
        btn_frame = Frame(labelframeleft, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        add_btn = Button(btn_frame,command=self.add_data, text="ADD",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        add_btn.grid(row=0, column=0, padx=1,pady=1)

        update_btn = Button(btn_frame,command=self.update_data, text="UPDATE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        update_btn.grid(row=0, column=1, padx=1,pady=1 )

        delete_btn = Button(btn_frame,command=self.delete_data, text="DELETE",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        delete_btn.grid(row=0, column=2, padx=1,pady=1 )    

        reset_btn = Button(btn_frame,command=self.reset_data, text="RESET",  width=10, font=("times new roman", 12, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        reset_btn.grid(row=0, column=3, padx=1,pady=1)

         # ================== table frame ========================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("times new roman", 12, "bold"), padx=2)   
        table_frame.place(x=600, y=50, width=600, height=350)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame, columns=("floor","roomno","roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table['show']='headings'

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100) 
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ================= add data function ========================

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
             messagebox.showerror("Error", "All Fields are required", parent=self.root) 
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                                                                        self.var_floor.get(),
                                                                        self.var_roomno.get(),
                                                                        self.var_roomtype.get()
                                                                                        ))
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)


    # ================== fetch data =================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

    # ===================== update ========================================================
    def update_data(self):
        if self.var_floor.get()=="":
             messagebox.showerror("Error", "Please enter mobile number", parent=self.root) 
        else:
               
                    conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update details set Floor=%s, RoomNo=%s, RoomType=%s where RoomNo=%s",(
                        
                                                                                                    self.var_floor.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomtype.get()
                                                                                                   
                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "New Room details has been updated successfully", parent=self.root)


     # ========================== Delete data =================================
    def delete_data(self):
        delete_data=messagebox.askyesno("Hotel Management System", "Do you want to delete this room details?", parent=self.root)
        if delete_data > 0:
              conn = mysql.connector.connect(host="localhost", username="root",  database="hotel_management")
              my_cursor = conn.cursor()
              query = "delete from details where RoomNo=%s"
              value = (self.var_roomno.get(),)
              my_cursor.execute(query, value)
        else:
            if not delete_data:
                     return 
        conn.commit()
        self.fetch_data()
        conn.close()


     # ======================== Reset data ============================
    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")  
       

        

if __name__ == "__main__":
    root = Tk()
    obj = RoomDetails(root)
    root.mainloop()