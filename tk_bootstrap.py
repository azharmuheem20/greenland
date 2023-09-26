import ttkbootstrap as tb
from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
 


class BootStrapp(tb.Window):
    def __init__(self, root):
        self.root = root
        self.root.title("TkBootstrap")
        self.root.geometry("900x700")
        style = tb.Style('darkly')
        
        #frames layout
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure((0,1,2,3), weight=0)
        
        #creating frames
        self.right_frame = ScrolledFrame(self.root, bootstyle='warning')
        self.right_frame.grid(row=0, column=0)

        self.center_frame = ScrolledFrame(self.root, bootstyle='danger')
        self.center_frame.grid(row=0, column=1, columnspan=2, rowspan=4, sticky='nsew')
        self.left_frame = ScrolledFrame(self.root, bootstyle='success')
        self.left_frame.grid(row=0, column=2)
        #frames gridding
        
        '''label = tb.Label(self.left_frame, text="This is Ttkbootstrap", font=("helvetica",20))
        label.grid(row=0, column=1, sticky='nsew')'''
        
        
        
        
        
if __name__=="__main__":
    root = tb.Window()
    app = BootStrapp(root)
    root.mainloop()