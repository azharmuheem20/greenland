#importing required modules
import tkinter
import customtkinter
from PIL import ImageTk,Image
from gui.userdashbord import UserDashbord
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

from database.db import DBHelper

class LoginScreen():
    def __init__(self,root):
        self.root = root
        self.root.geometry("600x440")
        self.root.title('Login')

        self.img1=ImageTk.PhotoImage(Image.open("pattern.png"))
        l1=customtkinter.CTkLabel(master=self.root,image= self.img1)
        l1.pack()

#creating custom frame
        frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
        l2.place(x=50, y=45)

        entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
        entry1.place(x=50, y=110)

        entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)

        l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
        l3.place(x=155,y=195)

        #Create custom button
        button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=self.button_function, corner_radius=6)
        button1.place(x=50, y=240)

    def button_function(self):
        self.root.destroy()            # destroy current window and creating new one 
        self.root = customtkinter.CTk()  
        app = UserDashbord(self.root)
        self.root.mainloop()
# You can easily integrate authentication system 


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = LoginScreen(root)
    root.mainloop()