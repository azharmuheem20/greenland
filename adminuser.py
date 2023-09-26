import tkinter 
from tkinter import ttk
import customtkinter
import random
import ttkbootstrap.constants as tbs
import mysql.connector


class AdminUser:
    def __init__(self,root,right_sidebar_frame,center_frame):
        self.root = root
        self.right_sidebar_frame = right_sidebar_frame
        self.center_frame = center_frame


    def user_sidebar_frame(self):
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        label = customtkinter.CTkLabel(self.right_sidebar_frame,text="Manage Users")
        label.grid(row=0, column=0)

        self.sidebar_button_names = ["View Users","Add Users","Update / Delete"]
        self.button_funcs = [self.view_users,self.add_users,self.update_delete_users]
        for i, e in enumerate (self.sidebar_button_names):
            self.buttons = customtkinter.CTkButton(self.right_sidebar_frame,text=e,command=self.button_funcs[i])
            self.buttons.grid(row = i+1, column=0, padx=20,pady=(10,5))

        return self.right_sidebar_frame

    def view_users(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(1,weight=1)
        self.center_frame.grid(row=0, column=1,sticky='nsew', rowspan=4, columnspan=2)

        conn = mysql.connector.connect(username="root",host="localhost",password="Azhar123@",database="greenland")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows= cursor.fetchall()

        label = customtkinter.CTkLabel(self.center_frame,text="View users",font=('calibari',30,'bold'))
        label.grid(row=0, column=1)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12,'bold')) # Modify the font of the body
        s.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        s.configure('mystyle.Treeview', rowheight=40)

        tree = ttk.Treeview(self.center_frame, column=("c1", "c2", "c3"),style="mystyle.Treeview", show='headings',height=14,selectmode ='browse')
        tree.grid(row=1, column=1,sticky='nsew')
        products_col = ['Username','User_ID', "User_Password"]
        i = 1
        for e in products_col:
            tree.column(f"# {i}",anchor=tkinter.CENTER, width=80)
            tree.heading(f"# {i}", text=e)
            i=i+1
            print(i,e)
        tree.tag_configure("Number", background="#FFB785")
        tree.tag_configure("Weight", background="#CEFF4C")
        tree.insert("",'end', values=rows)
        
        print('view users button clicked')
        return self.center_frame
    
    def add_users(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(1,weight=1)
        self.center_frame.grid(row=0, column=1,sticky='nsew', rowspan=4, columnspan=2)
        label = customtkinter.CTkLabel(self.center_frame,text="Add new user")
        label.grid(row=0, column=1)

        id_label = customtkinter.CTkLabel(self.center_frame,text="User_ID")
        id_label.grid(row=1, column=0, sticky='w', padx=20,pady=(10,5))
        user_id = random.randint(1000,9999)
        self.id_entry = customtkinter.CTkEntry(self.center_frame)
        self.id_entry.delete(0,'end')
        self.id_entry.insert(0,user_id)
        self.id_entry.grid(row=1, column=1, sticky='nsew', padx=20,pady=(10,5))
        name_label = customtkinter.CTkLabel(self.center_frame,text="User Name")
        name_label.grid(row=2, column=0, sticky='w', padx=20,pady=(10,5))
        self.name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Enter username')
        self.name_entry.grid(row=2, column=1, sticky='nsew', padx=20,pady=(10,5))
        pass_label = customtkinter.CTkLabel(self.center_frame,text="Password")
        pass_label.grid(row=3, column=0, sticky='w', padx=20,pady=(10,5))
        self.pass_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text='Enter password')
        self.pass_entry.grid(row=3, column=1, sticky='nsew', padx=20,pady=(10,5))
        add_button = customtkinter.CTkButton(self.center_frame,text="Add User")
        add_button.grid(row=4, column=1, sticky='nsew', padx=20,pady=(10,5))

        
        

        print('add user button clicked')
        return self.center_frame
    
    def update_delete_users(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root,corner_radius=8)
        self.center_frame.columnconfigure(1,weight=1)
        self.center_frame.grid(row=0, column=1,sticky='nsew', rowspan=4, columnspan=2)

        label = customtkinter.CTkLabel(self.center_frame,text="Update / Delete Users",font=('calibari',30,'bold'))
        label.grid(row=0, column=1)
        self.id_entry = customtkinter.CTkEntry(self.center_frame)
        self.id_entry.grid(row=1, column=1, sticky='nsew', padx=20,pady=(10,5))
        self.name_entry = customtkinter.CTkEntry(self.center_frame)
        self.name_entry.grid(row=2, column=1, sticky='nsew', padx=20,pady=(10,5))
        self.pass_entry = customtkinter.CTkEntry(self.center_frame)
        self.pass_entry.grid(row=3, column=1, sticky='nsew', padx=20,pady=(10,5))
        update_button = customtkinter.CTkButton(self.center_frame,text="Update User")
        update_button.grid(row=4, column=1, sticky='nsew', padx=20,pady=(10,5))
        del_button = customtkinter.CTkButton(self.center_frame,text="Delete User")
        del_button.grid(row=5, column=1, sticky='nsew', padx=20,pady=(10,5))
        
        """s = ttk.Style()
        s.theme_use('clam')
        s.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12,'bold')) # Modify the font of the body
        s.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings
        s.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        s.configure('mystyle.Treeview', rowheight=30)# Remove the borders"""

        self.tree = ttk.Treeview(self.center_frame, column=("c1", "c2",'c3'), show='headings',height=30)
        self.tree.grid(row=6, column=1,sticky='nsew')
        products_col = ['User_ID','Username','Password']
        i = 1
        for e in products_col:
            self.tree.column(f"# {i}",anchor=tkinter.CENTER, width=80)
            self.tree.heading(f"# {i}", text=e)
            i=i+1
            print(i,e)
        self.tree.tag_configure("Number", background="#FFB785")
        self.tree.tag_configure("Weight", background="#CEFF4C")

        data = [(123,'Azhar','S3cretp@ss')]
        for i in data:
            self.tree.insert("",'end',values=i)

        print('update/delete user button clicked')
        self.tree.bind("<<TreeviewSelect>>",self.selection)
        return self.center_frame


    def selection(self, event):
        self.id_entry.delete(0,'end')
        self.name_entry.delete(0,'end')
        self.pass_entry.delete(0,'end')

        select_record = self.tree.selection()
        value = self.tree.item(select_record,'values')

        self.id_entry.insert(0, value[0])
        self.name_entry.insert(0,value[1])
        self.pass_entry.insert(0,value[2])

        self.tree.bind("<<ReleaseButton-1>>",select_record)
        