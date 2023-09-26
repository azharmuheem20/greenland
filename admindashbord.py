# class AdminDashbord(customtkinter.CTk):
from tkinter import *
import tkinter
from tkinter import ttk
import tkinter.messagebox as MessageBox
import customtkinter
from time import strftime
import mysql.connector

# from database.db import DBHelper
from adminproduct import AdminProduct
from adminuser import AdminUser
from admincash import AdminCash
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


class AdminDashbord(customtkinter.CTk):
    def __init__(self,root):
        self.root = root
        self.button_funtions = [self.sidebar_button_one_event, self.sidebar_button_two_event, self.sidebar_button_three_event, self.sidebar_button_four_event, self.product_win, self.sidebar_button_six_event, self.sidebar_button_seven_event, self.sidebar_button_eight_event, self.sidebar_button_nine_event]
        self.button_names = ["View Cash Details","Manage Users","Manage Room","Manage Table","Manage Products","Manage Waiters","Manage Orders","Logout","Manage Couter"]
        print(len(self.button_names))
        print(len(self.button_funtions))
        self.root.resizable(width = 1, height = 1)
        # configure window
        self.root.title("Green Land Hotel & Restaurant")
        self.root.geometry(f"{1100}x{880}")

        # configure grid layout (4x4)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure((0, 1, 2,3), weight=1)
        self.theme = "light blue"
        self.right_sidebar_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        
        # create sidebar frame with widgets
        sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar_frame.grid_rowconfigure(9, weight=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame, text="Admin Here", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        for i,e in enumerate(self.button_names):
            sidebar_button = customtkinter.CTkButton(sidebar_frame, command=self.button_funtions[i], text=e)
            sidebar_button.grid(row=i+1, column=0, padx=20, pady=10)
        appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))
        scaling_label = customtkinter.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")

        scaling_label = customtkinter.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
        scaling_label.grid(row=14, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        scaling_optionemenu.grid(row=15, column=0, padx=20, pady=(10, 20))

        ac = AdminCash(self.root,self.right_sidebar_frame,self.center_frame)

        self.center_frame = ac.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
        
        self.right_sidebar_frame = ac.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        # set default values
        # sidebar_button_3.configure(state="disabled", text="Manage Rooms")
      
        appearance_mode_optionemenu.set("Dark")
        scaling_optionemenu.set("100%")
    
    # ____________________ Products  Start ________________
    # ____________________ PRODUCT END   ________________
    # user frame
    # ____________________ USER  Start ________________
    # ____________________ USER  END ________________
    # ____________________ Cash Status Start ________________
    # ____________________ Cash Status End ________________
    
    #product window
    def product_win(self):
        self.new_window = Toplevel(self.root)
        self.new_app = AdminProduct(self.new_window)
    
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.theme = new_appearance_mode
        print(new_appearance_mode )

    def change_scaling_event(self, new_scaling: str):
        try:
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
        except:
            pass
   # Cash Details
    def sidebar_button_one_event(self):
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        ac = AdminCash(self.root,self.right_sidebar_frame,self.center_frame)
        self.right_sidebar_frame = ac.cash_status_right_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = ac.cash_status_center_frame()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
      
         
        print("Admin sidebar_button cash status click")
    # user
    def sidebar_button_two_event(self):
        print("User Button click")
        self.center_frame.destroy()
        self.right_sidebar_frame.destroy()
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.root, width=140, corner_radius=8)
        # self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        au = AdminUser(self.root,self.right_sidebar_frame,self.center_frame)
        self.right_sidebar_frame = au.user_sidebar_frame()
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")
        self.center_frame = au.view_users()
        self.center_frame.grid(row=0, column=1, rowspan=4, columnspan=2 , sticky="nsew")
      
    def sidebar_button_three_event(self):
        print("sidebar_button click")
   
    def sidebar_button_four_event(self):
        print("sidebar_button click")
        
   # Mange Products
    def product_win(self):
        self.new_window = Toplevel(self.root)
        self.new_app = AdminProduct(self.new_window)
        
    def sidebar_button_six_event(self):
        print("sidebar_button click")
   
    def sidebar_button_seven_event(self):
        print("sidebar_button click")
   
    def sidebar_button_eight_event(self):
        print("sidebar_button click")
   
    def sidebar_button_nine_event(self):
        print("sidebar_button click")
        
    


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = AdminDashbord(root)
    root.mainloop()