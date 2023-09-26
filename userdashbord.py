import tkinter
import tkinter.messagebox
import customtkinter
from time import strftime
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import random

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


class UserDashbord():
    def __init__(self,root):
        self.root = root
        # configure window
        self.root.title("Green Land Hotel & Restaurant")


        # configure grid layout (4x4)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure((0, 1, 2,3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="User Name Here", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_one_event, text="Cash Status")
        sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_two_event, text="Hotel Purchase")
        sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_three_event, text="Book A Room")
        sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_four_event, text="Parcel Order")
        sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_five_event, text="Room Order")
        sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_six_event, text="Table Order")
        sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_seven_event, text="View All Orders")
        sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        sidebar_button_8 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_eight_event, text="Logout")
        sidebar_button_8.grid(row=8, column=0, padx=20, pady=10)
        sidebar_button_9 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_nine_event, text="Cancel / Edit Order")
        sidebar_button_9.grid(row=9, column=0, padx=20, pady=10)
        appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))
        scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")

        scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        scaling_optionemenu.grid(row=15, column=0, padx=20, pady=(10, 20))
        # self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        # self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        
        self.center_frame = self.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        
        self.right_sidebar_frame = self.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        
        # set default values
        
        #sidebar_button_3.configure(state="disabled", text="Book A Room")
      
        appearance_mode_optionemenu.set("Dark")
        scaling_optionemenu.set("100%")
 

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        print(new_appearance_mode )

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
#    Cash Status
    def sidebar_button_one_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
      
        
        print("sidebar_button cash status click")
   # Hotel Purschse
    def sidebar_button_two_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.hotel_purshase_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.hotel_purshase_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
    #room bokking    
    def sidebar_button_three_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.room_book_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.room_book_sidebar_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        print("room order button clicked")

#    Parcel Order
    def sidebar_button_four_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.parcel_order_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.parcel_order_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        print("Parcel oredr button clicked")
    def sidebar_button_five_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.room_order_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.room_order_sidebar_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        print("sidebar_button click")
   
    def sidebar_button_six_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.table_order_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.table_order_sidebar_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        print("sidebar_button click")
   
    def sidebar_button_seven_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = self.view_all_order_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        self.right_sidebar_frame = self.view_all_order_sidebar_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        print("sidebar_button click")
#    Logout event
    def sidebar_button_eight_event(self):
        self.root.destroy()            # destroy current window and creating new one 
   
    def sidebar_button_nine_event(self):
        print("sidebar_button click")
        
    def my_time(self):
        time_string = strftime('%H:%M:%S %p \n %A \n %x ')
        self.time_label.configure(text=time_string, text_color=("#2D75B3","white"))
        self.time_label.after(1000,self.my_time)
    
    # Cash Status Farames
    def cash_status_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(0, weight=1)
        name_label = customtkinter.CTkLabel(self.center_frame, text="Green Land Hotel & Restaurant", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        name_label = customtkinter.CTkLabel(self.center_frame, text="", font=customtkinter.CTkFont(size=40, weight="bold"))
        name_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        name_label = customtkinter.CTkLabel(self.center_frame, text="Available Cash : 84,110 PKR", font=customtkinter.CTkFont(size=40, weight="bold"))
        name_label.grid(row=2, column=0, padx=20, pady=(20, 10))
        name_label = customtkinter.CTkLabel(self.center_frame, text="Waiters Cash : 84,11 PKR", font=customtkinter.CTkFont(size=40, weight="bold"))
        name_label.grid(row=3, column=0, padx=20, pady=(20, 10))
        name_label = customtkinter.CTkLabel(self.center_frame, text="Canceled Ammount : 84,11 PKR", font=customtkinter.CTkFont(size=40, weight="bold"))
        name_label.grid(row=4, column=0, padx=20, pady=(20, 10))
        name_label = customtkinter.CTkLabel(self.center_frame, text="Hotel Purchase : 84,11 PKR", font=customtkinter.CTkFont(size=40, weight="bold"))
        name_label.grid(row=5, column=0, padx=20, pady=(20, 10))
        
        return self.center_frame
    
    def cash_status_right_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)
        self.time_label = customtkinter.CTkLabel(self.right_sidebar_frame, font=customtkinter.CTkFont(size=24, weight="bold"))
        self.time_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.my_time()
        '''right_button = customtkinter.CTkButton(self.right_sidebar_frame, command=self.sidebar_button_one_event, text="Cash Status")
        right_button.grid(row=0, column=0, padx=20, pady=10)'''
        
        recent_transection_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="Recent Activites", font=customtkinter.CTkFont(size=16, weight="bold"),width=120,height=25,fg_color=("#2D75B3", "white"), corner_radius=8,text_color=("white","#2D75B3"))
        recent_transection_label.grid(row=3, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+10000 Room Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=4, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+20000 Table Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=5, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+10000 Parcel Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=6, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="-10000 Fish Purchase", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#DA0037","#DA0037"))
        transection1_label.grid(row=7, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+10000 Room Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=8, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="-10000 Milk Purchase", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#DA0037","#DA0037"))
        transection1_label.grid(row=9, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+10000 Room Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=10, column=0, padx=20, pady=(20, 10))
        transection1_label = customtkinter.CTkLabel(master=self.right_sidebar_frame,text="+10000 Room Ordder", font=customtkinter.CTkFont(size=16, weight="bold"),text_color=("#2D75B3","white"))
        transection1_label.grid(row=11, column=0, padx=20, pady=(20, 10))
        
        return self.right_sidebar_frame
    
    # Hotel Purshase
    def hotel_purshase_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(0, weight=1)
        
        name_label = customtkinter.CTkLabel(self.center_frame, text="Hotel Purchase page", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        
        return self.center_frame
    
    def hotel_purshase_right_frame(self):
    
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)
        return self.right_sidebar_frame
     
    def save(self):
        id = self.customer_id_entry.get()
        customer = self.customer_entry.get()
        product = self.product_entry.get()
        pr_qty = self.product_qty_entry.get()
        pr_price = self.product_price_entry.get()
        if self.customer_entry.get()=="" or self.product_entry.get()=="" or self.product_qty_entry.get()=="" or self.product_price_entry.get()=="":
            messagebox.showerror("Error !", "Please, Do not leave any filed empty")
        else:
            conn = mysql.connector.connect(host="localhost", user="root",password="Azhar123@",database="greenland")
            cursor = conn.cursor()
            query = "INSERT INTO parcel (customer_id,customer_name,product_name,product_qty, product_price) VALUES (%s,%s, %s,%s,%s)"
            values = (id,customer, product, pr_qty,pr_price)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Message","Bill Saved Successfully")
            self.customer_id_entry.delete(0,'end')
            self.customer_entry.delete(0,'end')
            self.product_entry.delete(0, 'end')
            self.product_qty_entry.delete(0, 'end')
            self.product_price_entry.delete(0, 'end')
            self.customer_entry.focus_set()  
            conn.close()


    def pay(self):
        if self.customer_entry.get()=="" or self.product_entry.get()=="" or self.product_qty_entry.get()=="" or self.product_price_entry.get()=="":
            messagebox.showerror(title="Error !", message="Please enter complete details. ")
        else:
            self.totalprice = int(self.product_qty_entry.get())*int(self.product_price_entry.get())
            if (self.totalprice==0):
                messagebox.showerror(title="Error !", message="Product Quantity or Product Price is missing. ")
            else:
                customer_name_label = customtkinter.CTkLabel(self.label_frame, text=f"CustomerID : {self.customer_id_entry.get()}", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                customer_name_label.grid(row=0, column=0, sticky="w")
                customer_name_label = customtkinter.CTkLabel(self.label_frame, text=f"Customer Name : {self.customer_entry.get()}", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                customer_name_label.grid(row=1, column=0, sticky="w")
                pr_qty_label = customtkinter.CTkLabel(self.label_frame, text=f"Product Name : {self.product_entry.get()}", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                pr_qty_label.grid(row=2, column=0, sticky="w")
                pro_qty_label = customtkinter.CTkLabel(self.label_frame, text=f"Product Quantity : "+str(self.product_qty_entry.get()), font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                pro_qty_label.grid(row=3, column=0, sticky="w")
                pro_price_label = customtkinter.CTkLabel(self.label_frame, text=f"Product Price : "+ str(self.product_price_entry.get()), font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                pro_price_label.grid(row=4, column=0, sticky="w")
                pro_tprice_label = customtkinter.CTkLabel(self.label_frame, text=f"Total price : "+ str(self.totalprice), font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","black"))
                pro_tprice_label.grid(row=5, column=0, sticky="w")
                label = customtkinter.CTkLabel(self.label_frame, text="                                  Thanks for giving us a chance to serve you ❤", font=customtkinter.CTkFont(size=10, weight="bold"),text_color=("#2D75B3","Green"))
                label.grid(row=6, column=0, sticky="w")

                self.customer_entry.focus_set()


    
    # Parcel order Farames
    def parcel_order_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure((1), weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=10, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Parcel order page", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, sticky="nsew")
        #order 
        customer_name = customtkinter.CTkLabel(self.center_frame, text="Customer ID", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        customer_name.grid(row=1, column=0, sticky="w",padx=10, pady=(1,20))
        self.cust_id = random.randint(100, 9999)
        self.customer_id_entry = customtkinter.CTkEntry(self.center_frame, width=300)
        self.customer_id_entry.grid(row=1, column=1, sticky="nsew",padx=10, pady=(1,20))
        self.customer_id_entry.delete(0,'end')
        self.customer_id_entry.insert(0,self.cust_id)
        customer_name = customtkinter.CTkLabel(self.center_frame, text="Customer Name", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        customer_name.grid(row=2, column=0, sticky="w",padx=10, pady=(1,20))
        self.customer_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Customer here")
        self.customer_entry.grid(row=2, column=1, sticky="nsew",padx=10, pady=(1,20))
        product_name_label = customtkinter.CTkLabel(self.center_frame, text="Product Name", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        product_name_label.grid(row=3, column=0, sticky="w",padx=10, pady=(1,20))
        self.product_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Product")
        self.product_entry.grid(row=3, column=1, sticky="nsew",padx=10, pady=(1,20))
        pro_qty_label = customtkinter.CTkLabel(self.center_frame, text="Product Quantity", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        pro_qty_label.grid(row=4, column=0, sticky="w",padx=10, pady=(1,20))
        self.product_qty_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Product Quantity")
        self.product_qty_entry.grid(row=4, column=1, sticky="nsew",padx=10, pady=(1,20))
        product_price_label = customtkinter.CTkLabel(self.center_frame, text="Product Price", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        product_price_label.grid(row=5, column=0, sticky="w",padx=10, pady=(1,20))
        self.product_price_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Product Price")
        self.product_price_entry.grid(row=5, column=1, sticky="nsew",padx=10, pady=(1,20))
        bill_button = customtkinter.CTkButton(self.center_frame, text="Print bill",command=self.pay, corner_radius=12, cursor="hand2", width=300)
        bill_button.grid(row=6, column=1, sticky="nsew",padx=10, pady=(1,20))
        save_bill_button = customtkinter.CTkButton(self.center_frame, text="Save bill",command=self.save, corner_radius=12, cursor="hand2", width=300)
        save_bill_button.grid(row=7, column=1, sticky="nsew",padx=10, pady=(1,20))
        
        self.label_frame = ttk.LabelFrame(self.center_frame,text="Bill Payment details", width=500, height=300)
        self.label_frame.grid(row=8, column=1, sticky="nsew")




        db = mysql.connector.connect(host = "localhost", user = "root", password = "Azhar123@", database = "greenland")
        my_cursor = db.cursor()
        query= f'SELECT * FROM Products;'
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        db.close()
        for i, row in enumerate(rows):
            print(row)
        

        
        
        return self.center_frame
  
    def parcel_order_right_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)
        return self.right_sidebar_frame

    def room_booking(self):
        id = self.customer_id_entry.get()
        customer = self.customer_entry.get()
        room = self.room_no_entry.get()
        type = self.room_type.get()
        if self.customer_entry.get()=="" or self.room_no_entry.get()=="":
            messagebox.showerror("Error !", "Enter Customer name & room number")
        else:
            conn = mysql.connector.connect(host="localhost", user="root",password="Azhar123@",database="greenland")
            cursor = conn.cursor()
            query = "INSERT INTO rooms (room_no,customer_id,customer_name, room_type) VALUES (%s, %s,%s,%s)"
            values = (room,id,customer, type)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Message","Room Booked Successfully")
            self.customer_id_entry.delete(0,'end')
            self.customer_entry.delete(0,'end')
            self.room_no_entry.delete(0,'end')
            self.room_no_entry.focus_set()

            conn.close()

    def room_book_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure((1), weight=2)
        self.center_frame.grid(row=0, column=1, rowspan=10, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Room Booking", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, sticky="nsew")
        #order 
        customerid_name = customtkinter.CTkLabel(self.center_frame, text="Customer ID", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        customerid_name.grid(row=1, column=0, sticky="w",padx=10, pady=(1,20))
        self.customer_id_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Customer ID")
        self.customer_id_entry.grid(row=1, column=1, sticky="nsew",padx=10, pady=(1,20))
        customer_name = customtkinter.CTkLabel(self.center_frame, text="Customer Name", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        customer_name.grid(row=2, column=0, sticky="w",padx=10, pady=(1,20))
        self.customer_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Customer name")
        self.customer_entry.grid(row=2, column=1, sticky="nsew",padx=10, pady=(1,20))
        room_no_label = customtkinter.CTkLabel(self.center_frame, text="Room no. ", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_no_label.grid(row=3, column=0, sticky="w",padx=10, pady=(1,20))
        self.room_no_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Enter room number")
        self.room_no_entry.grid(row=3, column=1, sticky="nsew",padx=10, pady=(1,20))
        room_type_label = customtkinter.CTkLabel(self.center_frame, text="Room Type", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_type_label.grid(row=4, column=0, sticky="w",padx=10, pady=(1,20))
        ops= ("A/C", "Non-A/C")
        self.room_type = customtkinter.CTkComboBox(self.center_frame, values=ops, state="readonly")
        self.room_type.grid(row=4, column=1, sticky="nsew",padx=10, pady=(1,20))
        self.room_type.set("A/C")
        
        """product_price_label = customtkinter.CTkLabel(self.center_frame, text="Product Price", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        product_price_label.grid(row=4, column=0, sticky="w",padx=10, pady=(1,20))
        self.product_price_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Product Price")
        self.product_price_entry.grid(row=4, column=1, sticky="nsew",padx=10, pady=(1,20))"""
        bill_button = customtkinter.CTkButton(self.center_frame, text="Book room",command=self.room_booking, corner_radius=12, cursor="hand2", width=300)
        bill_button.grid(row=6, column=1, sticky="nsew",padx=10, pady=(1,20))

        return self.center_frame

    def room_book_sidebar_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure((1), weight=2)
        self.right_sidebar_frame.grid(row=0, column=1, rowspan=10, columnspan=2 , sticky="nsew")
        view_rooms_button = customtkinter.CTkButton(self.right_sidebar_frame, text="View Room details", cursor="hand2")
        view_rooms_button.grid(row=0,rowspan=10, column=0, padx=10, pady=(1,20))
      
    
    
        return self.right_sidebar_frame
    
    def room_order_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure((1), weight=2)
        self.center_frame.grid(row=0, column=1, rowspan=10, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Room Order", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, sticky="nsew")
        #order 
        room_no = customtkinter.CTkLabel(self.center_frame, text="Room Number", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_no.grid(row=1, column=0, sticky="w",padx=10, pady=(1,20))
        self.room_number_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Room No. ")
        self.room_number_entry.grid(row=1, column=1, sticky="nsew",padx=10, pady=(1,20))
        room_order = customtkinter.CTkLabel(self.center_frame, text="Room Order", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_order.grid(row=2, column=0, sticky="w",padx=10, pady=(1,20))
        self.room_order_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Order name")
        self.room_order_entry.grid(row=2, column=1, sticky="nsew",padx=10, pady=(1,20))
        save_bill_button = customtkinter.CTkButton(self.center_frame, text="Cofrim order", corner_radius=12, cursor="hand2", width=300)
        save_bill_button.grid(row=3, column=1, sticky="nsew",padx=10, pady=(1,20))

        return self.center_frame
    

    def table_order_sidebar_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)
    
        return self.right_sidebar_frame


    def table_order_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure((1), weight=2)
        self.center_frame.grid(row=0, column=1, rowspan=10, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Table Order", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, sticky="nsew")
        #order 
        room_no = customtkinter.CTkLabel(self.center_frame, text="Table Number", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_no.grid(row=1, column=0, sticky="w",padx=10, pady=(1,20))
        self.room_number_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Table No. ")
        self.room_number_entry.grid(row=1, column=1, sticky="nsew",padx=10, pady=(1,20))
        room_order = customtkinter.CTkLabel(self.center_frame, text="Table Order", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        room_order.grid(row=2, column=0, sticky="w",padx=10, pady=(1,20))
        self.room_order_entry = customtkinter.CTkEntry(self.center_frame, width=300, placeholder_text="Order name")
        self.room_order_entry.grid(row=2, column=1, sticky="nsew",padx=10, pady=(1,20))
        save_bill_button = customtkinter.CTkButton(self.center_frame, text="Cofrim order", corner_radius=12, cursor="hand2", width=300)
        save_bill_button.grid(row=3, column=1, sticky="nsew",padx=10, pady=(1,20))

        return self.center_frame


    def room_order_sidebar_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)
        '''view_rooms_button = customtkinter.CTkButton(self.right_sidebar_frame, text="View Room details")
        view_rooms_button.grid(row=0, column=0)'''
    
        return self.right_sidebar_frame
    

    def view_all_order_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=10, sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="View all Orders", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=0, sticky="nsew")
        """connection = mysql.connector.connect(host="localhost", username="root",password="Azhar123@", database="greenland")
        print("connected with DB.....")

        cursor = connection.cursor()
        query = "SELECT * FROM orders"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()"""

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12,'bold')) # Modify the font of the body
        s.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        s.configure('mystyle.Treeview', rowheight=40)# Remove the borders

        tree = ttk.Treeview(self.center_frame, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',style="mystyle.Treeview",height=14,selectmode ='browse')
        tree.grid(row=1, column=0,sticky='nsew')
        products_col = ["ProductID","Product_name","Category","OrderType","Price","CustomerName"]
        i = 1
        for e in products_col:
            tree.column(f"# {i}",anchor=tkinter.CENTER, width=100)
            tree.heading(f"# {i}", text=e)
            i=i+1
            print(i,e)
        tree.tag_configure("Number", background="#FFB785")
        tree.tag_configure("Weight", background="#CEFF4C")
            # tree.insert(''', 'end', text=f"{i}", values=row)
        """for i, row in enumerate(rows):
            print(row)
            tree.insert('', 'end', text=f"{i}", values=row,tag=row[2])"""
        
        vsb = ttk.Scrollbar(self.center_frame, orient="vertical", command=tree.yview)
        vsb.grid(row=1, column=1, sticky="ns")
        hsb = ttk.Scrollbar(self.center_frame, orient="horizontal", command=tree.xview)
        hsb.grid(row=2, column=0, sticky="ew")
        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

        

        return self.center_frame
    
    def view_all_order_sidebar_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.right_sidebar_frame.columnconfigure(0, weight=1)


    
        return self.right_sidebar_frame

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = UserDashbord(root)
    root.mainloop()