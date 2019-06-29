import tkinter
from Point import Point
from Color import Color

class Graphics ( ):
    def __init__ ( self, root = tkinter.Tk, width = int, height = int , color = Color):
        self.root = root
        self.canvas = tkinter.Canvas ( self.root , width = width , height = height, bg = color  )
    def create_rectangle ( self , startPoint = Point(), endPoint = Point (), color = Color ):
        self.canvas.create_rectangle ( startPoint.x , startPoint.y , endPoint.x , endPoint.y , bg = Color , width = 0 )

    def create_text ( self, startPoint = Point() , text1 = str, font1 = str, anchor1 = None, color = Color ):
        if anchor1 == None :
            self.canvas.create_text ( startPoint.x, startPoint.y , text = text1 , font = font1 , fill = color )
        else:
            self.canvas.create_text ( startPoint.x , startPoint.y , text = text1, font = font1 , fill = color , anchor = anchor1 )