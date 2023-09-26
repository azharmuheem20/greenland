import tkinter
from tkinter import ttk
import tkinter.messagebox as MessageBox
import customtkinter
from time import strftime

# from database.db import DBHelper

class AdminCash:  
    def __init__(self,root,right_sidebar_frame,center_frame):
        self.root = root
        self.right_sidebar_frame = right_sidebar_frame
        self.center_frame = center_frame
        
    def cash_status_center_frame(self):
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=8)
        self.center_frame.columnconfigure(0, weight=1)
        name_label = customtkinter.CTkLabel(self.center_frame, text="Green Land Hotel & Restorent", font=customtkinter.CTkFont(size=40, weight="bold", underline=True),text_color=("#2D75B3","white"))
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
        # right_button = customtkinter.CTkButton(self.right_sidebar_frame, command=self.sidebar_button_one_event, text="Cash Status")
        # right_button.grid(row=0, column=0, padx=20, pady=10)
        
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
    
    def my_time(self):
        time_string = strftime('%H:%M:%S %p \n %A \n %x ')
        self.time_label.configure(text=time_string, text_color=("#2D75B3","white"))
        self.time_label.after(1000,self.my_time)
