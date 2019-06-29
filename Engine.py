import tkinter
import Frames
from Graphics import Graphics
import Animation
from data import Data
from id import *
import KeyEvent
from m10_controlbox import Controlbax
class Engine(object):
    """ 가계부 핵심 엔진입니다 """

    def __init__ ( self, root = tkinter.Tk ):
        self.root = root 
        self.이벤트중인수 = 0
        self.data = Data()
        #self.data.testData()
        self.data.MakeViewData ( "날자" )
        self.g = tkinter.Canvas ( root ,width = 1400, height = 800, bg = Frames.Color.c3 )
        self.controlbox = Controlbax ( engine = self )
        self.event = KeyEvent.event( self )

        ##self.root.bind("<Key>", self._EventKey ) ###키 이벤트 발생
        
        #########처음 로딩 화면
        #self.g = tkinter.Canvas ( root ,width = 1400, height = 800, bg = Frames.Color.c3 )
        self.g.create_text ( 700 , 400 , fill = "#FFFFFF" , font = "맑은고딕 34 bold", text = "Tip:\n오른쪽 클릭으로 추가 컨트롤 박스가 나타납니다.\n데이타 추가창에서 탭키를 활용하여 생산성을 높이세요!" )
        self._Start_Frame()
        self._Start_Frame_pStart ( )
        self.root.after ( 3000 , self.Main_Frame.Active , True , self )
        ############################################################################################
        self.start_ment = "가계부 버전 : m13"
        self.Warning_Frame.창바.text.text = self.start_ment ## 다 로딩 되고 추가적으로 마지막에 실행할것 있으면 이벤트 항목 참고
        ############################################################################################
        self.root.after ( 3000 , self.Warning_Frame.Active , True , self )
        self.g.place ( x = -2 , y = 0 , width = 1400, height = 800)

    def ThreadStart ( self ):
        """ 화면을 주기적으로 그려줍니다 ThreadEnd를 꼭 사용하세요 """
        self.이벤트중인수 =self.이벤트중인수 + 1
        print("-------------------------ThreadStart---------------")
        if self.이벤트중인수 == 1:
            self.__Thread()
    def ThreadEnd ( self ):
        """ 스택구조처럼 작용됩니다. 스래드 하나를 제거합니다"""
        if self.이벤트중인수 > 0:
            print("-------------------------ThreadEnd---------------")
            self.이벤트중인수 =self.이벤트중인수 - 1



    def __Thread ( self ):
        """thread """
        print("1")
        self.g.delete ( "all" )
        self.g.create_image ( 700,400, image = self.backImage )# r\과제
        self.Main_Frame.Draw ( self.g )
        self.Graph_Frame.Draw( self.g )
        self.Plus_Frame.Draw ( self.g )
        self.View_Frame.Draw ( self.g )
        self.Warning_Frame.Draw( self.g)
        self.controlbox.Draw()
        if self.이벤트중인수 > 0:
            self.root.after ( 20 , self.__Thread )
    def _Start_Frame ( self ):
        """ 사용할 프레임을 여기다 정의 하세요"""
        self.Main_Frame = Frames.Main()
        self.Main_Frame.Start ( self.g )
        self.Main_Frame.Enable( True )
        self.Main_Frame.Visible (  )

        self.Graph_Frame = Frames.Graph()
        self.Graph_Frame.Enable ( False)
        self.Graph_Frame.Visible ( False )

        self.View_Frame = Frames.View ( )
        self.View_Frame.Start ( self.g )
        self.View_Frame.Enable ( False )
        self.View_Frame.Visible ( False )

        self.Plus_Frame = Frames.Plus ()
        self.Plus_Frame.Start ( self.g )
        self.Plus_Frame.Enable ( False )
        self.Plus_Frame.Visible ( False )

        self.Warning_Frame = Frames.WarningFrame()
        self.Warning_Frame.Start ( self.g )
        self.Warning_Frame.Enable ( False )
        self.Warning_Frame.Visible (False )
        self.controlbox.Frame()
    def _Start_Frame_pStart ( self ):
        """ 처음 애니메이션을 위해 모든 항목의 크기를 조절합니다 """
        self.Main_Frame.메인.pSize.y = 0
        self.Main_Frame.내역.pSize.y = 0
        self.Main_Frame.추가.pSize.y = 0
        self.Main_Frame.종료.pSize.y = 0
        self.Main_Frame.상태바.pSize.x = 0
        self.Main_Frame.빈공간.pSize.x = 0

        self.Graph_Frame.아래바.pSize.x = 0
        self.Graph_Frame.전체바.pSize.y = 0
        self.Graph_Frame.첫바.pSize.y = 0
        self.Graph_Frame.둘바.pSize.y = 0
        self.Graph_Frame.삼바.pSize.y = 0
        self.Graph_Frame.넷바.pSize.y = 0
        self.Graph_Frame.오바.pSize.y = 0
        self.Graph_Frame.전체이름.pSize.y = 0
        self.Graph_Frame.첫이름.pSize.y = 0
        self.Graph_Frame.둘이름.pSize.y = 0
        self.Graph_Frame.삼이름.pSize.y = 0
        self.Graph_Frame.넷이름.pSize.y = 0
        self.Graph_Frame.오이름.pSize.y = 0
        self.Graph_Frame.전체그래프.pSize.y = 0
        self.Graph_Frame.첫그래프.pSize.y = 0
        self.Graph_Frame.둘그래프.pSize.y = 0
        self.Graph_Frame.삼그래프.pSize.y = 0
        self.Graph_Frame.넷그래프.pSize.y = 0
        self.Graph_Frame.오그래프.pSize.y = 0

        self.View_Frame.큰바.pSize.x = 0
        self.View_Frame.창바.pSize.x = 0
        self.View_Frame.작은바.pSize.x = 0
        self.View_Frame.이전글.pSize.x = 0
        self.View_Frame.다음글.pSize.x = 0
        self.View_Frame.날자.pSize.y = 0
        self.View_Frame.금액.pSize.y = 0
        self.View_Frame.태그.pSize.y = 0
        self.View_Frame.내용.pSize.y = 0
        self.View_Frame.날자글.pSize.y = 0
        self.View_Frame.금액글.pSize.y = 0
        self.View_Frame.태그글.pSize.y = 0
        self.View_Frame.내용글.pSize.y = 0

        self.Plus_Frame.큰바.pSize.x = 0
        self.Plus_Frame.창바.pSize.x = 0
        self.Plus_Frame.작은바.pSize.x = 0
        self.Plus_Frame.설명글.pSize.x = 0
        self.Plus_Frame.날자.pSize.y = 0
        self.Plus_Frame.금액.pSize.y = 0
        self.Plus_Frame.태그.pSize.y = 0
        self.Plus_Frame.내용.pSize.y = 0
        self.Plus_Frame.날자글.pSize.y = 0
        self.Plus_Frame.금액글.pSize.y = 0
        self.Plus_Frame.태그글.pSize.y = 0
        self.Plus_Frame.내용글.pSize.y = 0