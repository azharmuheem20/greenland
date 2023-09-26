import ttkbootstrap as tbs
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
import customtkinter


class TwoFrame(tbs.Window):
    def __init__(self, root):
        self.root = root
        self.root.title("TwoFrames")
        self.root.geometry("500x400")
        style = tbs.Style("darkly")
        
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure((0,1,2), weight=1)
        # self.root.columnconfigure(1,weight=1)
        
        
        
        self.right_frame = customtkinter.CTkFrame(self.root, corner_radius=15)
        self.right_frame.grid(row=0, column=0, rowspan=4, sticky='ns')
        button = customtkinter.CTkButton(self.right_frame, text="Button", cursor="hand2")
        button.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.left_frame = customtkinter.CTkFrame(self.root, corner_radius=15)
        self.left_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", rowspan=4)



if __name__=="__main__":
    root = tbs.Window()
    app = TwoFrame(root)
    root.mainloop()