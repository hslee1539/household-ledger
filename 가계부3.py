from tkinter import *
import 미션8모듈
import Engine
import id
import Color

root = Tk()
root.title("201401985")
#root.configure ( bg = Color.Color.c2 )
root.geometry ( "1396x789") # 1400 x 800이지만, 캔번스가 정의된것보다 -2작음 한마디로 보정한 결과.
root.resizable(width = False , height = False )

미션8모듈.M8( root )


engine = Engine.Engine( root )
engine.backImage = PhotoImage ( file = "back.png" )
id.engine = engine
id.g = engine.g
root.mainloop ()
engine.data.save()