from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import RoomDetails



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x700+0+0")

        # ====================== logo ==========================
        imglogo = Image.open(r"C:\Hotel Management\Images\logohotel.png")
        imglogo = imglogo.resize((230, 130), Image.Resampling.LANCZOS) 
        self.photoimage1 = ImageTk.PhotoImage(imglogo)

        lblimglogo = Label(image=self.photoimage1, bg="black", borderwidth=0)  
        lblimglogo.place(x=0, y=0, width=230, height=130)

        # ================== hotel img =======================
        img2 = Image.open(r"C:\Hotel Management\Images\hotel1.png")
        img2 = img2.resize((1500, 130), Image.Resampling.LANCZOS) 
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)  
        lblimg2.place(x=230, y=0, width=1500, height=130)

        # =============== title ===========================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", borderwidth=4, relief=RIDGE)
        lbl_title.place(x=0, y=130, width=1550, height=50)

        # ================== main frame ========================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=180, width=1550, height=620)

        # ================= menu ==========================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", borderwidth=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================= btn frame ========================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)   
        btn_frame.place(x=0, y=35, width=228, height=160)   

        # ================= buttons ========================
        cust_btn = Button(btn_frame,command=self.cust_details, text="CUSTOMER",  width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)  

        room_btn = Button(btn_frame,command=self.room_booking, text="ROOM",  width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame,command=self.room_details, text="DETAILS",  width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)   

        # report_btn = Button(btn_frame, text="REPORT",  width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        # report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame,command=self.logout, text="LOGOUT",  width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", borderwidth=0, cursor="hand1")
        logout_btn.grid(row=3, column=0, pady=1)


        # ================= right side image ========================
        img3 = Image.open(r"C:\Hotel Management\Images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS) 
        self.photoimage3 = ImageTk.PhotoImage(img3) 
        lblimg3 = Label(main_frame, image=self.photoimage3, borderwidth=0, relief=RIDGE)  
        lblimg3.place(x=230, y=0, width=1310, height=590)

        # ================= down image ========================
        img4 = Image.open(r"C:\Hotel Management\Images\\myh.jpg")
        img4 = img4.resize((1550, 210), Image.Resampling.LANCZOS) 
        self.photoimage4 = ImageTk.PhotoImage(img4)     
        lblimg4 = Label(main_frame, image=self.photoimage4, borderwidth=0, relief=RIDGE)  
        lblimg4.place(x=0, y=200, width=225, height=210)

        img5 = Image.open(r"C:\Hotel Management\Images\khana.jpg")
        img5 = img5.resize((230, 210), Image.Resampling.LANCZOS) 
        self.photoimage5 = ImageTk.PhotoImage(img5)     
        lblimg5 = Label(main_frame, image=self.photoimage5, borderwidth=0, relief=RIDGE)  
        lblimg5.place(x=0, y=420, width=225, height=190)


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)    

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)    

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomDetails(self.new_window)    

    def logout(self):
        self.root.destroy()

    
        

      

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()