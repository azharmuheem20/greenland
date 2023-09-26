import customtkinter
# class AdminDashbord(customtkinter.CTk):
import tkinter
from tkinter import ttk
import tkinter.messagebox as MessageBox
from time import strftime
import mysql.connector

#from database.db import DBHelperProducts

class AdminProduct(customtkinter.CTk):
    def __init__(self,root):
        self.root = root
        # configure grid layout (4x4)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure((0, 1, 2,3), weight=1)
        self.theme = 'light blue'
        
        #self.category_list = ["Value 2", "Value "]

        self.sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Products", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_one_event, text="Cash Status")
        sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_two_event, text="Products Purchases")
        sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_three_event, text="Product sales")
        sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_four_event, text="Parcel Orders")
        sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_five_event, text="Room Orders")
        sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_six_event, text="Table Orders")
        sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_seven_event, text="View All Products")
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
        
        self.center_frame = self.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4 , sticky="nsew")
        
        self.right_sidebar_frame = self.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        
        appearance_mode_optionemenu.set("Dark")
        scaling_optionemenu.set("100%")
 

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        print(new_appearance_mode )

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def sidebar_button_one_event(self):        
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        self.center_frame = self.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.right_sidebar_frame = self.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
      
    
    def sidebar_button_two_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        self.center_frame = self.view_product_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4 , sticky="nsew")
        self.right_sidebar_frame = self.product_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        
    
    def sidebar_button_three_event(self):
        pass
    
    def sidebar_button_four_event(self):
        pass
    
    def sidebar_button_five_event(self):
        pass
    
    def sidebar_button_six_event(self):
        pass
    
    def sidebar_button_seven_event(self):
        pass
    
    def sidebar_button_eight_event(self):
        pass
    
    def sidebar_button_nine_event(self):
        pass
    
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
        name_label = customtkinter.CTkLabel(self.center_frame, text="Logged-in at : 09:30 am", font=customtkinter.CTkFont(size=20, weight="bold"))
        name_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Last User : Xyz", font=customtkinter.CTkFont(size=20, weight="bold"))
        name_label.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        
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
        

 #================================add product====================
    def add_product(self):
        product_id = self.id_entry.get()
        product_name = self.name_entry.get()
        product_cat = self.category_entry.get()
        product_qty = self.qty_entry.get()
        product_price = self.price_entry.get()
        if self.name_entry.get()=="" or self.category_entry.get()=="" or self.price_entry.get()=="" or self.qty_entry.get()=="":
             MessageBox.showerror("Information","Please, enter complete data ! ")
        else:
              conn = mysql.connector.connect(host="localhost", user="root",password="Azhar123@",database="greenland")
              cursor = conn.cursor()
              #========Add new Records/users========

              query = "INSERT INTO products (id,product_name,product_category, product_qty, product_price) VALUES (%s, %s,%s, %s, %s)"
              values = (product_id,product_name, product_cat, product_qty, product_price)
              cursor.execute(query, values)
              conn.commit()
              MessageBox.showinfo("Information","Record Inserted successfully") 
              self.id_entry.delete(0,'end')
              self.name_entry.delete(0,'end')
              self.category_entry.delete(0, 'end')
              self.qty_entry.delete(0, 'end')
              self.price_entry.delete(0, 'end')
              self.name_entry.focus_set()  
              conn.close()

    # UI Frames
    def product_right_frame(self):
        self.button_names_p = ["View All Products","Create Product","Update / Delete Product"]
        self.button_funtions_p = [self.view_product_frame,self.create_product_frame,self.update_product_frame]
        
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        logo_label = customtkinter.CTkLabel(self.right_sidebar_frame, text="Manage Products", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        for i,e in enumerate(self.button_names_p):
            r_sidebar_button = customtkinter.CTkButton(self.right_sidebar_frame, command=self.button_funtions_p[i], text=e)
            r_sidebar_button.grid(row=i+1, column=0, padx=20, pady=10)

        return self.right_sidebar_frame

    def create_product_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure((1), weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=4 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Create A Product", font=customtkinter.CTkFont(size=32, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, sticky="nsew")

        id_label = customtkinter.CTkLabel(self.center_frame, text="Product ID", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        id_label.grid(row=1, column=0, sticky="w",padx=10, pady=5)
        self.id_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Product ID")
        self.id_entry.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        product_name_label = customtkinter.CTkLabel(self.center_frame, text="Product Name", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        product_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Name of Product', width=500)
        self.name_entry.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        category_label2 = customtkinter.CTkLabel(self.center_frame, text="Product Category", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        category_label2.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.category_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Category of Product', width=500)
        self.category_entry.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)
        qty_label = customtkinter.CTkLabel(self.center_frame, text="Product Qty", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        qty_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.qty_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Qty of Product', width=500)
        self.qty_entry.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)
        price_label = customtkinter.CTkLabel(self.center_frame, text="Product Price", font=customtkinter.CTkFont(size=20, weight="bold"),text_color=("#2D75B3","white"))
        price_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.price_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Price of Product', width=500)
        self.price_entry.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)
        submit_button = customtkinter.CTkButton(self.center_frame, text="Submit", command=self.add_product)
        submit_button.grid(row=7, column=1, sticky="nsew", padx=10, pady=5)
        
        return 
    
    def view_product_frame(self):
        #self.right_sidebar_frame.destroy()
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="View All Products", font=customtkinter.CTkFont(size=32, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=1, padx=20, pady=(20, 10))
      
        connection = mysql.connector.connect(host="localhost", username="root",password="Azhar123@", database="greenland")
        print("connected with DB.....")

        cursor = connection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        """s = ttk.Style()
        s.theme_use('default')
        s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12,'bold')) # Modify the font of the body
        s.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        s.configure('mystyle.Treeview', rowheight=40)"""# Remove the borders

        tree = ttk.Treeview(self.center_frame, column=("c1", "c2", "c3","c4","c5"), show='headings',height=14)
        
        products_col = ["ProductID","Category","QtyType","Name","Price"]
        i = 1
        for e in products_col:
            tree.column(f"# {i}",anchor=tkinter.CENTER, width=80)
            tree.heading(f"# {i}", text=e)
            i=i+1
            print(i,e)
        tree.tag_configure("Number", background="#FFB785")
        tree.tag_configure("Weight", background="#CEFF4C")
        tree.grid(row=1, column=1,sticky='nsew')
            # tree.insert(''', 'end', text=f"{i}", values=row)
        for i, row in enumerate(rows):
            print(row)
            tree.insert('', 'end', text=f"{i}", values=row,tag=row[2])

        '''vsb = ttk.Scrollbar(self.tree, orient="vertical", command=tree.yview)
        vsb.grid(row=1, column=1)
        hsb = ttk.Scrollbar(self.tree, orient="horizontal", command=tree.xview)
        hsb.grid(row=2, column=0)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)'''
            

        return self.center_frame
        
    def update_product_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Update / Delete Product", font=customtkinter.CTkFont(size=32, weight="bold", underline=True),text_color=("#2D75B3","white"))
        name_label.grid(row=0, column=0,columnspan=2, padx=20, pady=(20, 10),sticky="nsew")
            
         # Product entries   
        self.id_entry_u = customtkinter.CTkEntry(self.center_frame, placeholder_text="ID")
        self.id_entry_u.grid(row=2, column=1, padx=10, pady=5,sticky="nsew")
        self.name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Product Name")
        self.name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
        self.category_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Product Category")
        self.category_entry.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")
        self.qty_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Quantity of Product")
        self.qty_entry.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")
        self.price_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Price of Product")
        self.price_entry.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")
        
        #Buttons
        self.update_button = customtkinter.CTkButton(self.center_frame, text="Update Product",command=self.update_product)
        self.update_button.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")
        self.delete_button = customtkinter.CTkButton(self.center_frame, text="Delete Product",state="enabled", command=lambda: self.delete_product(self.id_entry_u.get()))
        self.delete_button.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")
        self.delete_all_button = customtkinter.CTkButton(self.center_frame, text="Delete All Product", command=lambda: self.delete_all_product())
        self.delete_all_button.grid(row=10, column=1, padx=10, pady=5, sticky="nsew")
        
        connection = mysql.connector.connect(host="localhost", username="root",password="Azhar123@", database="greenland")
        print("connected with DB.....")

        cursor = connection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        
        #s = ttk.Style()
        '''s.theme_use('default')
        s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12,'bold')) # Modify the font of the body
        s.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        s.configure('mystyle.Treeview', rowheight=40)'''
        self.tree = ttk.Treeview(self.center_frame, column=("c1", "c2", "c3","c4","c5"), show='headings',height=7)
        
        products_col = ["ProductID","Category","QtyType","Name","Price"]
        i = 1
        for e in products_col:
            self.tree.column(f"# {i}",anchor=tkinter.CENTER, width=80)
            self.tree.heading(f"# {i}", text=e)
            i=i+1
            print(i,e)
        self.tree.tag_configure("Number", background="#FFB785")
        self.tree.tag_configure("Weight", background="#CEFF4C")
        self.tree.grid(row=1, column=1,sticky='nsew')
            # tree.insert(''', 'end', text=f"{i}", values=row)
        for i, row in enumerate(rows):
            print(row)
            self.tree.insert('', 'end', text=f"{i}", values=row,tag=row[2])

        print('update/delete user button clicked')
        self.tree.bind("<<TreeviewSelect>>",self.selection)
        return self.center_frame


    def selection(self, event):
        self.id_entry_u.delete(0,'end')
        self.name_entry.delete(0,'end')
        self.category_entry.delete(0,'end')
        self.qty_entry.delete(0, 'end')
        self.price_entry.delete(0,'end')

        select_record = self.tree.selection()
        value = self.tree.item(select_record,'values')

        self.id_entry_u.insert(0, value[0])
        self.name_entry.insert(0,value[1])
        self.category_entry.insert(0,value[2])
        self.qty_entry.insert(0, value[3])
        self.price_entry.insert(0,value[4])

        self.tree.bind("<<ReleaseButton-1>>",select_record)
        
    
    # Database functions
    
    def update_product(self):
        id = self.id_entry_u.get()
        name = self.name_entry.get()
        category = self.category_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()

        if (id == '' or name == '' or category =="" or qty =="" or price == ''):
            MessageBox.showinfo("ALERT", "Please enter fields you want to Update!")
            return
        else:
            conn = mysql.connector.connect(host="localhost", username="root",password="Azhar123@", database="greenland")
            cursor = conn.cursor()
            query = "UPDATE products SET product_name = %s, product_category = %s, product_qty = %s, product_price = %s WHERE id = %s"
            values = (id, name, category, qty, price)
            cursor.execute(query, values)
            conn.commit()
            if cursor.rowcount >= 0:
                MessageBox.showinfo("Status", "Successfully Updated")
            else:
                MessageBox.showinfo("Information", "No records updated")
                conn.close()
            #self.clear_values()
                
            print("Button Pressed")
    """def delete_product(self, id):
        if id == "":
            MessageBox.showinfo("ALERT","ID is required to select row!")
        else:
            try:
                db = DBHelperProducts()
                db.delete_product(id)
                MessageBox.showinfo("Status", "Successfully Deleted")
            except:
                MessageBox.showwarning("Error", "Please Cheak your value")
            finally:
                self.set_state_for_update_and_delete()
                self.clear_values()
    def select_product(self,id):
        if id == "":
            MessageBox.showinfo("ALERT","ID is required to select row!")
        else:
            try:
                self.name_entry.delete(0,customtkinter.END)
                self.price_entry.delete(0,customtkinter.END)
                db = DBHelperProducts()
                row = db.select_product(id)[0]
                print(row)
                self.category_entry.set(row[1])
                self.qty_entry.set(row[2])
                self.name_entry.insert(0, row[3])
                self.price_entry.insert(0, row[4])
                self.set_state_for_select()
                
                
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print (message)
                MessageBox.showwarning("Error", message)
    
    def create_product(self,category,qty_type,name,price):
        if (category == '' or qty_type == '' or name == '' or price == ''):
            MessageBox.showinfo("ALERT", "Please enter fiels you want to Create!")
            return
        else:
            try:
                db = DBHelperProducts()
                db.create_product(category,qty_type,name,price)
                MessageBox.showinfo("Status", "Successfully Inserted")
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print (message)
                MessageBox.showwarning("Error", "Please Cheak your value")
            finally:
                self.name_entry.delete(0,customtkinter.END)
                self.price_entry.delete(0,customtkinter.END)
                try:
                    db = DBHelperProducts()
                    new_id = db.get_last_id()[0][0] + 1
                except:
                    new_id = ""
                self.id_entry_c.configure(text=new_id)
                
    def delete_all_product(self):
        ok = MessageBox.askokcancel("Delete","Do you want to delete all products ?")
        if ok:
            try:
                db = DBHelperProducts()
                db.delete_all_product()
                MessageBox.showinfo("Success","You have deleted all products")
            except Exception as ex:
                print(ex)
                MessageBox.showerror("Error","Operation failed")
    # Set State
    def clear_values(self):
        self.name_entry.delete(0,customtkinter.END)
        self.price_entry.delete(0,customtkinter.END)
        self.id_entry_u.delete(0,customtkinter.END)
    
    def set_state_for_update_and_delete(self):
        self.select_button.configure(state="enabled")
        self.id_entry_u.configure(state="normal")
        self.update_button.configure(state="enabled")
        self.delete_button.configure(state="enabled")
    
    def set_state_for_select(self):
        self.update_button.configure(state="enabled")
        self.delete_button.configure(state="enabled")
        self.select_button.configure(state="enabled")
        self.delete_all_button.configure(state="enabled")
        self.id_entry_u.configure(state="readonly")
    
    # Set Scroolbar
    def scrollbars(self,tree):
    # Y Scrol Bar
        yscrollbar = customtkinter.CTkScrollbar(self.center_frame, orientation='vertical', command=tree.yview, button_hover_color=("#4DCFFF","#CEFF4C"))
        yscrollbar.grid(row=1, column=1, sticky='ns')
        tree.configure(yscrollcommand=yscrollbar.set)
        # yscrollbar.configure(command=tree.yview)
        
        # X Scrol Bar
        xscrollbar = customtkinter.CTkScrollbar(self.center_frame, orientation='horizontal', command=tree.xview, button_hover_color=("#4DCFFF","#CEFF4C"))
        xscrollbar.grid(row=2, column=0, sticky='ew')
        tree.configure(xscrollcommand=xscrollbar.set)"""
    
    
if __name__=="__main__":
    root = customtkinter.CTk()
    app = AdminProduct(root)
    root.mainloop()