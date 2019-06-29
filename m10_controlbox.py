import tkinter
import Text
import Color
import Frames
class Controlbax:
    """ 오른쪽 클릭을 하면 아래에 추가 동작을 선택할 수 있는 컨트롤 박스를 만듭니다. """
    def __init__(self, **kwargs):
        """ 컨트롤 박스를 만들기 위해 engine값이 필요합니다. """
        self.__sw = 0
        self.StrVar설명글 = tkinter.StringVar ( )
        self.engine = kwargs["engine"]
        self.__Frame = tkinter.Frame ( self.engine.root )
        self.secondCanvas = tkinter.Canvas ( self.engine.root , bg = Color.Color.c1 , width = '0')
        self.secondCanvas.place ( x = 1098, y = 800 , width = 300 , height = 100  )
        self.Label = tkinter.Label ( self.engine.root ,bg = Color.Color.c2,fg = Color.Color.c6 , font = Text.Text().font, textvariable = self.StrVar설명글,height = 3 , anchor = "w" )
        self.Label.place ( x = 0 ,  y= 800 , width = 1100 , height = 100 )
        self.StrVar설명글.set("test")
        self.engine.g.bind ( "<Button-3>" , self._RClick )
        self.engine.g.bind ( "<ButtonRelease-1>" , self._LClick )
    def Frame ( self ):
        """자체적으로 프래임들을 만듭니다. """
        self.그래프 = Frames.ControlFrame_Graph ()
        self.내역 = Frames.ControlFrame_View ()
        self.추가 = Frames.ControlFrame_Plus ()
        self.그래프.Start ( self.secondCanvas )
        self.내역.Start ( self.secondCanvas )
        self.추가.Start ( self.secondCanvas )
        self.그래프.Enable ( )
        self.내역.Enable()
        self.추가.Enable()
        self.그래프.Visible ( )
        self.내역.Visible ()
        self.추가.Visible()
    def Draw ( self ):
        """ 자체적으로 드로우 합니다. Thread에서 호출해주세요"""
        self.secondCanvas.delete ( "all")
        self.그래프.Draw(self.secondCanvas)
        self.내역.Draw(self.secondCanvas)
        self.추가.Draw(self.secondCanvas)


    def _LClick ( self , event ):
        """ 왼쪽 클릭시 클릭박스는 사라져야 합니다. """
        print(" y = ", event.y )
        print(" x = ", event.x )
        if self.__sw == 1:
            #if event.y > 100 or event.x > 300:
                self.__showBox()
    def _RClick ( self , event):
        """ 오른쪽 클릭을 했을때 동작을 설정합니다. """
        #self.__sw = 0
        self.__showBox()
    def Animation ( self):
        """ 애니메이션을 준비합니다 """
        if self.__sw == 0:
            self.__AnimationDown ( 0,20,0,1)
        else:
            self.__AnimationUp ( 0,20,0,1)
    def AnimationUp(self):
        """ 화면에서 사라지는 애니메이션입니다 """
        self.__sw = 1
        self.Animation()
    def __AnimationUp ( self , nowFrame, Frame, f , df ) :
        f = f + df
        ff = f + 1

        df = df + 3 * int((nowFrame/Frame) > 0.2 )

        dx = 100 * f / ff
        self.engine.g.place_configure ( height = 700 + dx )
        self.Label.place_configure ( y = 701 + dx ) ##원래는 700이지만, 캔번스가 정의되어 있는것보다 -2작으므로. 보정됨
        self.secondCanvas.place_configure ( y = 699 + dx )

        nowFrame = nowFrame + 1
        if nowFrame < Frame :
            self.engine.root.after ( 20 , self.__AnimationUp , nowFrame , Frame , f , df)
        else:
            self.engine.g.place_configure ( height = 800 )
            self.Label.place_configure ( y = 801 )
            self.secondCanvas.place_configure ( y = 799 )
            self.__sw = 0
    def __AnimationDown ( self , nowFrame, Frame, f , df ) :
        f = f + df
        ff = f + 1

        df = df + 3 * int((nowFrame/Frame) > 0.2 )

        dx = 100 * f / ff
        self.engine.g.place_configure ( height = 800 - dx )
        self.Label.place_configure ( y = 801 - dx ) ##원래는 700이지만, 캔번스가 정의되어 있는것보다 -2작으므로. 보정됨
        self.secondCanvas.place_configure ( y = 799 - dx )

        nowFrame = nowFrame + 1
        if nowFrame < Frame :
            self.engine.root.after ( 20 , self.__AnimationDown , nowFrame , Frame , f , df)
        else:
            self.engine.g.place_configure ( height = 700 )
            self.Label.place_configure ( y = 701 )
            self.secondCanvas.place_configure ( y = 699 )
            self.__sw = 1

    def __showBox ( self ):
        """ 컨트롤 박스를 보이게 합니다."""
        if self.engine.Graph_Frame.visible == True:
            self.StrVar설명글.set("다음 항목을 관리합니다.")
            self.그래프.Visible ( True )
            self.그래프.Enable ( True )
            self.내역.Visible (  )
            self.내역.Enable (  )
            self.추가.Visible (  )
            self.추가.Enable (  )
            self.Draw()
        elif self.engine.View_Frame.visible == True:
            self.그래프.Visible (  )
            self.그래프.Enable (  )
            self.내역.Visible (  True)
            self.내역.Enable ( True )
            self.추가.Visible (  )
            self.추가.Enable (  )
            self.Draw()
            self.StrVar설명글.set("현재 보고있는 데이타를 관리합니다.")
        elif self.engine.Plus_Frame.visible == True:
            self.그래프.Visible (  )
            self.그래프.Enable (  )
            self.내역.Visible (  )
            self.내역.Enable (  )
            self.추가.Visible ( True )
            self.추가.Enable ( True )
            self.Draw()
            self.StrVar설명글.set("추가 동작들 입니다.")

        self.Animation()
        
