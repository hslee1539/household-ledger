from tkinter import *
from sys import exit

class M8 ():
    def __init__(self , root = Tk):
        """M8전용 디버깅 박스"""
        self.root = root
        self.menu1= Menu( root )
        self.menu = Menu ( root )
        self.menu1.add_command (label = "강제종료", command = self.click )
        self.menu.add_cascade ( label = "디버깅", menu = self.menu1)
        root.config ( menu = self.menu )
        return super().__init__()
    def click (self):
        self.root.destroy( )
        exit()