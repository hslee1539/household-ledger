from Graphics import *
from Text import Text
import Object
import Animation
import data


class _Frame ():
    def Visible ( self, visible = False ):
        self.visible = visible
    def Draw ( self , g = tkinter.Canvas ):
        if self.visible == True:
            self._Draw (g )

    def _Draw ( self, g = tkinter.Canvas ):
        """ 여기다 그릴 것을 추가 하세요"""
    def Enable ( self , enable = False ):
        """이 프레임에 관련된 모든 이벤트를 사용할지 결정합니다."""
        self.enable = enable
        self._Enable()

    def _Enable ( self ):
        """ 여기다 이벤트 사용할 객체를 코딩하세요"""
    def Active ( self , start , engine):
        """ 이 프레임 전체를 애니메이션을 발생 시킵니다"""
    def Start ( self , root ):
        """ 이벤트를 등록시킬려면 여기다 코딩하세요"""
    def WaitActive ( self , start , engine ):
        """ 앞의 프레임 단위의 이벤트가 종료가 되면 실행을 합니다. 판단은 Engine.이벤트중인수 가  0이 되면 합니다. """
        self.__WaitActive__( start , engine )
    def __WaitActive__ ( self, start , engine ):
        if engine.이벤트중인수 == 0:
            engine.root.after ( 0 , self.Active , start , engine )
        else:
            engine.root.after ( 15 , self.__WaitActive__ , start , engine )



class Main (_Frame):
    """ 메인 프레임의 오브젝트들의 정의 """
    def __init__ ( self ):
        self.메인 = Object.iButton ( Point(0,0),Point(100,100), Object.Color.c1, "메인.메인",  "icon_graph.png")
        self.내역 = Object.iButton ( Point(100,0),Point(100,100), Object.Color.c1, "메인.내역", "icon_view.png")
        self.추가 = Object.iButton ( Point(200,0),Point(100,100), Object.Color.c1, "메인.추가", "icon_plus.png")
        self.빈공간 = Object.Box ( Point(300,0),Point(1000,100), Object.Color.c2, "메인.빈공간" )
        self.종료 = Object.iButton ( Point(1300,0),Point(100,100), Object.Color.c5, "메인.종료", "icon_exit.png")
        self.상태바 = Object.Label ( Point(0,100),Point(1400,100), Object.Color.c7, "메인.상태바", Text("개발중"))
        self.배경가림 = Object.Box ( Point ( 0 , 200 ) , Point(1400 , 550 ) , Object.Color.c7 , "메인.배경가림" )
    def Start ( self, root ):
        """이벤트를 등록합니다"""
        self.메인.Start( root , True )
        self.내역.Start( root , True )
        self.추가.Start( root , True )
        self.종료.Start( root , True )
    def Draw(self, g ):
        return super().Draw(g)
    def _Draw(self, g ):
        self.배경가림.Draw ( g )
        self.메인.Draw( g )
        self.내역.Draw( g )
        self.추가.Draw( g )
        self.빈공간.Draw( g )
        self.종료.Draw( g )
        self.상태바.Draw( g )
    def _Enable(self):
        self.메인.enable = self.enable
        self.내역.enable = self.enable
        self.추가.enable = self.enable
        self.종료.enable = self.enable
        return super()._Enable()
    def Active(self, start , engine):
        if start == True :
            engine.Main_Frame.상태바.text.text = "   그래프     조회       추가            (이중 버튼을 클릭하여 시작하세요)"
            engine.root.after ( 000 , self.Visible , True )
            engine.root.after ( 000 , Animation.SizeChange , self.상태바 , engine, 20 , Point(0,100) ,self.상태바.pSizeORIGEN)
            engine.root.after ( 000 , Animation.SizeChange , self.빈공간 , engine , 20 , Point(0,100) ,self.빈공간.pSizeORIGEN)
            engine.root.after ( 100 , Animation.SizeChange , self.메인 , engine, 20 , Point(100,0) ,self.메인.pSizeORIGEN)
            engine.root.after ( 200 , Animation.SizeChange , self.내역 , engine, 20 , Point(100,0) ,self.내역.pSizeORIGEN)
            engine.root.after ( 300 , Animation.SizeChange , self.추가 , engine, 20 , Point(100,0) ,self.추가.pSizeORIGEN)
            engine.root.after ( 400 , Animation.SizeChange , self.종료 , engine, 20 , Point(100,0) ,self.종료.pSizeORIGEN)
            engine.root.after ( 000 , Animation.SizeChange , self.배경가림 , engine, 20 , Point(1400,0) ,self.배경가림.pSizeORIGEN)
        else:
            engine.root.after ( 000 , Animation.SizeChange , self.상태바 , engine, 20 ,self.상태바.pSizeORIGEN, Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange , self.빈공간 , engine, 20 ,self.빈공간.pSizeORIGEN, Point(0,100) )
            engine.root.after ( 400 , Animation.SizeChange , self.메인 , engine, 20 ,self.메인.pSizeORIGEN, Point(100,0) )
            engine.root.after ( 300 , Animation.SizeChange , self.내역 , engine, 20 ,self.내역.pSizeORIGEN, Point(100,0) )
            engine.root.after ( 200 , Animation.SizeChange , self.추가 , engine, 20 ,self.추가.pSizeORIGEN, Point(100,0) )
            engine.root.after ( 100 , Animation.SizeChange , self.종료 , engine, 20 ,self.종료.pSizeORIGEN, Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange , self.배경가림 , engine, 20 ,self.배경가림.pSizeORIGEN, Point(1400,0) )
            engine.root.after ( 800 , self.Visible , False )
        return super().Active(start , engine )
class Graph ( _Frame ):
    """ id 이름 법칙 숫자는 한글자만 사용함 예) 첫번째 바 = 첫바, 둘바, 삼바, 넷바, 오바   (군대 포병숫자와 비슷)"""
    # 그래프 그릴때 바 색이 파랑색이니
    #        그래프 크기를 가지고 얼마나 가릴지 프로그래밍 하자
    #
    #
    def __init__( self ):
        self.아래바 = Object.Box ( Point ( 0 ,   600 ),Point (1400 , 100  ) , Object.Color.c2 , "그래프.아래바")
        self.전체바 = Object.Box ( Point ( 100 , 300 ),Point ( 100 , 400  ) , Object.Color.c3 , "그래프.전체바")
        self.첫바 = Object.Box ( Point ( 400 , 300 ),Point ( 100 , 300  ) , Object.Color.c3 , "그래프.첫바")
        self.둘바 = Object.Box ( Point ( 600 , 300 ),Point ( 100 , 300  ) , Object.Color.c3 , "그래프.둘바")
        self.삼바 = Object.Box ( Point ( 800 , 300 ),Point ( 100 , 300  ) , Object.Color.c3 , "그래프.삼바")
        self.넷바 = Object.Box ( Point ( 1000 ,300 ),Point ( 100 , 300  ) , Object.Color.c3 , "그래프.셋바")
        self.오바 = Object.Box ( Point ( 1200 ,300 ),Point ( 100 , 300  ) , Object.Color.c3 , "그래프.오바")
        self.전체이름 = Object.Label( Point ( 100 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.전체이름",Text ( "전체\n100%", None ) )
        self.첫이름 = Object.Label( Point ( 400 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.첫이름",Text ( "전체", None ) )
        self.둘이름 = Object.Label( Point ( 600 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.둘이름",Text ( "전체", None ) )
        self.삼이름 = Object.Label( Point ( 800 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.삼이름",Text ( "전체", None ) )
        self.넷이름 = Object.Label( Point (1000 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.넷이름",Text ( "전체", None ) )
        self.오이름 = Object.Label( Point (1200 , 600),Point ( 100 , 100 ) , Object.Color.c3 , " 그래프.오이름",Text ( "전체", None ) )
        self.전체그래프 = Object.Box ( Point ( 100 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.전체그래프")
        self.첫그래프 = Object.Box ( Point ( 400 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.첫그래프")
        self.둘그래프 = Object.Box ( Point ( 600 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.둘그래프")
        self.삼그래프 = Object.Box ( Point ( 800 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.삼그래프")
        self.넷그래프 = Object.Box ( Point (1000 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.넷그래프")
        self.오그래프 = Object.Box ( Point (1200 , 300 ) , Point ( 100, 300 ) , Object.Color.c2 , "그래프.오그래프")

    def _Draw(self, g = tkinter.Canvas):
        self.아래바.Draw ( g )
        self.전체바.Draw ( g )
        self.첫바.Draw ( g )
        self.둘바.Draw ( g )
        self.삼바.Draw ( g )
        self.넷바.Draw ( g )
        self.오바.Draw ( g )
        self.전체이름.Draw( g )
        self.첫이름.Draw( g )
        self.둘이름.Draw( g )
        self.삼이름.Draw( g )
        self.넷이름.Draw( g )
        self.오이름.Draw( g )
        self.전체그래프.Draw ( g )
        self.첫그래프.Draw ( g )
        self.둘그래프.Draw ( g )
        self.삼그래프.Draw ( g )
        self.넷그래프.Draw ( g )
        self.오그래프.Draw ( g )
        return super()._Draw(g)
    def Active(self, start, engine):
        if start == True:
            engine.root.after ( 0 , self.Visible , True )
            engine.Main_Frame.상태바.text.text = "  얼마나 사용했는지 그래프로 표시됩니다."
            engine.root.after ( 0 , Animation.SizeChange ,self.아래바 , engine, 20, Point(0,100) ,self.아래바.pSizeORIGEN)
            engine.root.after ( 200 , Animation.SizeChange ,self.전체바 , engine, 20 , Point ( 100 , 0 ), self.전체바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.첫바 , engine, 20 , Point ( 100 , 0 ), self.첫바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.둘바 , engine, 20 , Point ( 100 , 0 ), self.둘바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.삼바 , engine, 20 , Point ( 100 , 0 ), self.삼바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.넷바 , engine, 20 , Point ( 100 , 0 ), self.넷바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.오바 , engine, 20 , Point ( 100 , 0 ), self.오바.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.전체이름 , engine, 20 , Point ( 100 , 0 ), self.전체이름.pSizeORIGEN )
            engine.root.after ( 250 , Animation.SizeChange ,self.첫이름 , engine, 20 , Point ( 100 , 0 ), self.첫이름.pSizeORIGEN )
            engine.root.after ( 300 , Animation.SizeChange ,self.둘이름 , engine, 20 , Point ( 100 , 0 ), self.둘이름.pSizeORIGEN )
            engine.root.after ( 350 , Animation.SizeChange ,self.삼이름 , engine, 20 , Point ( 100 , 0 ), self.삼이름.pSizeORIGEN )
            engine.root.after ( 400 , Animation.SizeChange ,self.넷이름 , engine, 20 , Point ( 100 , 0 ), self.넷이름.pSizeORIGEN )
            engine.root.after ( 450 , Animation.SizeChange ,self.오이름 , engine, 20 , Point ( 100 , 0 ), self.오이름.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.전체그래프 , engine, 20 , Point ( 100 , 0 ), self.전체그래프.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.첫그래프 , engine, 20 , Point ( 100 , 0 ), self.첫그래프.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.둘그래프 , engine, 20 , Point ( 100 , 0 ), self.둘그래프.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.삼그래프 , engine, 20 , Point ( 100 , 0 ), self.삼그래프.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.넷그래프 , engine, 20 , Point ( 100 , 0 ), self.넷그래프.pSizeORIGEN )
            engine.root.after ( 200 , Animation.SizeChange ,self.오그래프 , engine, 20 , Point ( 100 , 0 ), self.오그래프.pSizeORIGEN )
            engine.root.after (1200 , Animation.SizeChange ,self.전체그래프 , engine, 40 , self.전체그래프.pSizeORIGEN , self.전체그래프.pSize보조 )
            engine.root.after (1200 , Animation.SizeChange ,self.첫그래프 , engine, 40 , self.첫그래프.pSizeORIGEN , self.첫그래프.pSize보조 )
            engine.root.after (1200 , Animation.SizeChange ,self.둘그래프 , engine, 40 , self.둘그래프.pSizeORIGEN , self.둘그래프.pSize보조 )
            engine.root.after (1200 , Animation.SizeChange ,self.삼그래프 , engine, 40 , self.삼그래프.pSizeORIGEN , self.삼그래프.pSize보조 )
            engine.root.after (1200 , Animation.SizeChange ,self.넷그래프 , engine, 40 , self.넷그래프.pSizeORIGEN , self.넷그래프.pSize보조 )
            engine.root.after (1200 , Animation.SizeChange ,self.오그래프 , engine, 40 , self.오그래프.pSizeORIGEN , self.오그래프.pSize보조 )
        else :
            engine.root.after ( 1450 , self.Visible , False )
            engine.root.after (0 , Animation.SizeChange ,self.전체그래프 , engine, 20 , self.전체그래프.pSize보조 , self.전체그래프.pSizeORIGEN )
            engine.root.after (0 , Animation.SizeChange ,self.첫그래프 , engine, 20 , self.첫그래프.pSize보조 , self.첫그래프.pSizeORIGEN )
            engine.root.after (0 , Animation.SizeChange ,self.둘그래프 , engine, 20 , self.둘그래프.pSize보조 , self.둘그래프.pSizeORIGEN )
            engine.root.after (0 , Animation.SizeChange ,self.삼그래프 , engine, 20 , self.삼그래프.pSize보조 , self.삼그래프.pSizeORIGEN )
            engine.root.after (0 , Animation.SizeChange ,self.넷그래프 , engine, 20 , self.넷그래프.pSize보조 , self.넷그래프.pSizeORIGEN )
            engine.root.after (0 , Animation.SizeChange ,self.오그래프 , engine, 20 , self.오그래프.pSize보조 , self.오그래프.pSizeORIGEN )
            engine.root.after (800 ,   Animation.SizeChange ,self.아래바 , engine, 20 ,self.아래바.pSizeORIGEN , Point( 0 , 100 )  )
            engine.root.after (1050 , Animation.SizeChange ,self.전체이름 , engine, 20 , self.전체이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (1000 , Animation.SizeChange ,self.첫이름 , engine, 20 , self.첫이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (950 , Animation.SizeChange ,self.둘이름 , engine, 20 , self.둘이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (900 , Animation.SizeChange ,self.삼이름 , engine, 20 , self.삼이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (850 , Animation.SizeChange ,self.넷이름 , engine, 20 , self.넷이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.오이름 , engine, 20 , self.오이름.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.전체바 , engine, 20 , self.전체바.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.첫바 , engine, 20 , self.첫바.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.둘바 , engine, 20 , self.둘바.pSizeORIGEN , Point( 100 , 0 ) ) 
            engine.root.after (800 , Animation.SizeChange ,self.삼바 , engine, 20 , self.삼바.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.넷바 , engine, 20 , self.넷바.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.오바 , engine, 20 , self.오바.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.전체그래프 , engine, 20 , self.전체그래프.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.첫그래프 , engine, 20 , self.첫그래프.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.둘그래프 , engine, 20 , self.둘그래프.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.삼그래프 , engine, 20 , self.삼그래프.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.넷그래프 , engine, 20 , self.넷그래프.pSizeORIGEN , Point( 100 , 0 ) )
            engine.root.after (800 , Animation.SizeChange ,self.오그래프 , engine, 20 , self.오그래프.pSizeORIGEN , Point( 100 , 0 ) )
        return super().Active(start, engine)

class View ( _Frame ):
    """ 여기다 내역 프레임의 정의하세요 """
    def __init__( self ): 
        """ """
        self.큰바 = Object.Box ( Point ( 0 , 300 ) , Point ( 1400 , 100 ) , Color.c2 , "내역.큰바" )
        self.창바 = Object.Box ( Point ( 500,300 ) , Point (  700 , 400 ) , Color.c2 , "내역.창바" )
        self.작은바=Object.Box ( Point ( 500,300 ) , Point (  700 , 100 ) , Color.c3 ,"내역.작은바")

        self.이전글 = Object.TextOnlyButton ( Point ( 0 , 300 ) , Point ( 500 , 100 ) , "내역.이전글" , Text( "테스트테스트테스트",None ) )
        self.다음글 = Object.TextOnlyButton ( Point (1200,300 ) , Point ( 200 , 100 ) , "내역.다음글" , Text( "테스트테스트",None ) )

        self.날자 = Object.TextOnlyButton ( Point ( 500 , 300 ) , Point ( 100 , 100 ) , "내역.날자" , Text ( "날자", None ) )
        self.금액 = Object.TextOnlyButton ( Point ( 500 , 400 ) , Point ( 100 , 100 ) , "내역.금액" , Text ( "금액", None ) )
        self.태그 = Object.TextOnlyButton ( Point ( 500 , 500 ) , Point ( 100 , 100 ) , "내역.태그" , Text ( "태그", None ) )
        self.내용 = Object.TextOnlyButton ( Point ( 500 , 600 ) , Point ( 100 , 100 ) , "내역.내용" , Text ( "내용", None ) )

        self.날자범위 = Object.ClickBox ( Point ( 500 , 300 ) , Point ( 700 , 100 ) , "내역.날자범위" )
        self.금액범위 = Object.ClickBox ( Point ( 500 , 400 ) , Point ( 700 , 100 ) , "내역.금액범위" )
        self.태그범위 = Object.ClickBox ( Point ( 500 , 500 ) , Point ( 700 , 100 ) , "내역.태그범위" )
        self.내용범위 = Object.ClickBox ( Point ( 500 , 600 ) , Point ( 700 , 100 ) , "내역.내용범위" )

        self.날자글 = Object.TextOnlyButton ( Point ( 600 , 300 ) , Point ( 600 , 100 ) , "내역.날자글" , Text ( "테스트테스트테스트테스트") )
        self.금액글 = Object.TextOnlyButton ( Point ( 600 , 400 ) , Point ( 600 , 100 ) , "내역.금액글" , Text ( "테스트테스트테스트테스트") )
        self.태그글 = Object.TextOnlyButton ( Point ( 600 , 500 ) , Point ( 600 , 100 ) , "내역.태그글" , Text ( "테스트테스트테스트테스트") )
        self.내용글 = Object.TextOnlyButton ( Point ( 600 , 600 ) , Point ( 600 , 100 ) , "내역.내용글" , Text ( "테스트테스트테스트테스트") )

        datass = data.Data()
        datass.MakeViewData( "날자" )
        datas = datass.MakeList()
        self.이전글.text.text = datas[0]
        self.다음글.text.text = datas[2]
        self.날자글.text.text = datas[1]["날자"]
        self.금액글.text.text = datas[1]["금액"]
        self.태그글.text.text = datas[1]["태그"]
        self.내용글.text.text = datas[1]["내용"]
    def _Draw(self, g = tkinter.Canvas):
        self.큰바.Draw ( g )
        self.창바.Draw ( g )
        self.작은바.Draw ( g )
        self.이전글.Draw ( g )
        self.다음글.Draw ( g )
        self.날자.Draw ( g )
        self.금액.Draw ( g )
        self.태그.Draw ( g )
        self.내용.Draw ( g )
        self.날자글.Draw ( g )
        self.금액글.Draw ( g )
        self.태그글.Draw ( g )
        self.내용글.Draw ( g )
        return super()._Draw(g)
    def Start ( self , root ):
        """ 이벤트 발생 준비를 합니다. enable = True가 되면 실행합니다 """
        self.이전글.Start ( root, True )
        self.다음글.Start ( root , True )
        self.날자범위.Start ( root , True )
        self.금액범위.Start ( root , True )
        self.태그범위.Start ( root , True )
        self.내용범위.Start ( root , True )
    def _Enable(self):
        self.이전글.enable = self.enable
        self.다음글.enable = self.enable
        self.날자범위.enable = self.enable
        self.금액범위.enable = self.enable
        self.태그범위.enable = self.enable
        self.내용범위.enable = self.enable
        return super()._Enable()
    def Active(self, start, engine):
        """ 엑티브 메소드는 프레임내 모든 이벤트 준비를 합니다"""
        if start == True:
            if engine.Warning_Frame.visible == False:
                self.Enable ( True )
            engine.root.after ( 000 , self.Visible , True )
            engine.Main_Frame.상태바.text.text = "  모든 데이타를 조회 합니다."
            engine.root.after ( 000 , Animation.SizeChange ,self.큰바, engine, 20, Point(0,100) , self.큰바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.창바, engine, 10 ,Point(0,400), self.창바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.작은바, engine, 20 ,Point(0,100), self.작은바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.이전글, engine, 20 ,Point(0,100), self.이전글.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.다음글, engine, 20 ,Point(0,100), self.다음글.pSizeORIGEN )
            engine.root.after (  55 , Animation.SizeChange_FastToSlow ,self.날자글, engine, 30 ,Point(100,0), self.날자글.pSizeORIGEN )
            engine.root.after ( 100 , Animation.SizeChange_FastToSlow ,self.금액글, engine, 25 ,Point(100,0), self.금액글.pSizeORIGEN )
            engine.root.after ( 145 , Animation.SizeChange_FastToSlow ,self.태그글, engine, 20 ,Point(100,0), self.태그글.pSizeORIGEN )
            engine.root.after ( 190 , Animation.SizeChange_FastToSlow ,self.내용글, engine, 15 ,Point(100,0), self.내용글.pSizeORIGEN )
            engine.root.after (  45 , Animation.SizeChange_FastToSlow ,self.날자, engine, 35 ,Point(100,0), self.날자.pSizeORIGEN )
            engine.root.after (  90 , Animation.SizeChange_FastToSlow ,self.금액, engine, 30 ,Point(100,0), self.금액.pSizeORIGEN )
            engine.root.after ( 135 , Animation.SizeChange_FastToSlow ,self.태그, engine, 25 ,Point(100,0), self.태그.pSizeORIGEN )
            engine.root.after ( 180 , Animation.SizeChange_FastToSlow ,self.내용, engine, 20,Point(100,0), self.내용.pSizeORIGEN )
        else:
            self.Enable ( False )
            engine.root.after ( 410 , self.Visible , False )
            engine.root.after ( 000 , Animation.SizeChange ,self.큰바, engine, 20 , self.큰바.pSizeORIGEN, Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.창바, engine, 10, self.창바.pSizeORIGEN ,Point(0,400) )
            engine.root.after ( 000 , Animation.SizeChange ,self.작은바, engine, 20 , self.작은바.pSizeORIGEN,Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.다음글, engine, 20 , self.다음글.pSizeORIGEN,Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.이전글, engine, 20 , self.이전글.pSizeORIGEN,Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.날자글, engine, 20 , self.날자글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.금액글, engine, 20 , self.금액글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.태그글, engine, 20 , self.태그글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.내용글, engine, 20 , self.내용글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.날자, engine, 20 , self.날자.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.금액, engine, 20 , self.금액.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.태그, engine, 20 , self.태그.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.내용, engine, 20, self.내용.pSizeORIGEN,Point(100,0) )
        return super().Active(start, engine)
class Plus ( _Frame ):
    """ 여기에다 추가 프레임을 정의 하세요"""
    def __init__ ( self ):
        self.큰바  =          Object.Box ( Point ( 0 , 300 ) , Point (1400 ,  100 ) , Color.c2 , "추가.큰바" )
        self.창바  =          Object.Box ( Point (600, 300 ) , Point ( 600 ,  400 ) , Color.c2 , "추가.창바" )
        self.작은바=          Object.Box ( Point (600, 300 ) , Point ( 600 ,  100 ) , Color.c3 , "추가.작은바" )
        self.설명글=Object.TextOnlyButton( Point ( 0 , 300 ) , Point ( 600 ,  100 ) , "추가.설명글", Text ( "먼저, 년도를 입력하세요", None ) )

        self.날자범위 = Object.ClickBox ( Point ( 600 , 300 ) , Point ( 600 , 100 ) , "추가.날자범위" )
        self.금액범위 = Object.ClickBox ( Point ( 600 , 400 ) , Point ( 600 , 100 ) , "추가.금액범위" )
        self.태그범위 = Object.ClickBox ( Point ( 600 , 500 ) , Point ( 600 , 100 ) , "추가.태그범위" )
        self.내용범위 = Object.ClickBox ( Point ( 600 , 600 ) , Point ( 600 , 100 ) , "추가.내용범위" )

        self.날자  =Object.TextOnlyButton( Point (600, 300 ) , Point ( 100 ,  100 ) , "추가.날자", Text ( "날자" , None ) )
        self.금액  =Object.TextOnlyButton( Point (600, 400 ) , Point ( 100 ,  100 ) , "추가.금액", Text ( "금액" , None ) )
        self.태그  =Object.TextOnlyButton( Point (600, 500 ) , Point ( 100 ,  100 ) , "추가.태그", Text ( "태그" , None ) )
        self.내용  =Object.TextOnlyButton( Point (600, 600 ) , Point ( 100 ,  100 ) , "추가.내용", Text ( "내용"  , None ) )
        self.날자글=Object.TextOnlyButton( Point (700, 300 ) , Point ( 500 ,  100 ) , "추가.날자글", Text ( "" ) )
        self.금액글=Object.TextOnlyButton( Point (700, 400 ) , Point ( 500 ,  100 ) , "추가.금액글", Text ( "" ) )
        self.태그글=Object.TextOnlyButton( Point (700, 500 ) , Point ( 500 ,  100 ) , "추가.태그글", Text ( "" ) )
        self.내용글=Object.TextOnlyButton( Point (700, 600 ) , Point ( 500 ,  100 ) , "추가.내용글", Text ( "" ) )

    def _Draw ( self , g = tkinter.Canvas ):
        self.큰바.Draw ( g )
        self.창바.Draw ( g )
        self.작은바.Draw ( g )
        self.설명글.Draw ( g )
        self.날자.Draw ( g )
        self.금액.Draw ( g )
        self.태그.Draw ( g )
        self.내용.Draw ( g )
        self.날자글.Draw ( g )
        self.금액글.Draw ( g )
        self.태그글.Draw ( g )
        self.내용글.Draw ( g )
    def Start ( self, root ):
        """ 이벤트를 등록합니다"""
        self.날자범위.Start ( root , True )
        self.금액범위.Start ( root , True )
        self.태그범위.Start ( root , True )
        self.내용범위.Start ( root , True )
    def _Enable(self):
        """ 각 요소들의 enable값을 내장된 self.enable로 대입합니다"""
        self.날자범위.enable = self.enable
        self.금액범위.enable = self.enable
        self.태그범위.enable = self.enable
        self.내용범위.enable = self.enable
        return super()._Enable()
    def Active(self, start, engine):
        if start == True:
            engine.root.after ( 0 , self.Visible , True )
            engine.root.after ( 0 , self.Enable , True )
            engine.Main_Frame.상태바.text.text = "  데이타를 추가합니다."
            engine.root.after ( 000 , Animation.SizeChange ,self.큰바, engine, 20, Point(0,100) , self.큰바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.창바, engine, 10 ,Point(0,400), self.창바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.작은바, engine, 20 ,Point(0,100), self.작은바.pSizeORIGEN )
            engine.root.after ( 000 , Animation.SizeChange ,self.설명글, engine, 20 ,Point(0,100), self.설명글.pSizeORIGEN )
            engine.root.after (  55 , Animation.SizeChange_FastToSlow ,self.날자글, engine, 30 ,Point(100,0), self.날자글.pSizeORIGEN )
            engine.root.after ( 100 , Animation.SizeChange_FastToSlow ,self.금액글, engine, 25 ,Point(100,0), self.금액글.pSizeORIGEN )
            engine.root.after ( 145 , Animation.SizeChange_FastToSlow ,self.태그글, engine, 20 ,Point(100,0), self.태그글.pSizeORIGEN )
            engine.root.after ( 190 , Animation.SizeChange_FastToSlow ,self.내용글, engine, 15 ,Point(100,0), self.내용글.pSizeORIGEN )
            engine.root.after (  45 , Animation.SizeChange_FastToSlow ,self.날자, engine, 35 ,Point(100,0), self.날자.pSizeORIGEN )
            engine.root.after (  90 , Animation.SizeChange_FastToSlow ,self.금액, engine, 30 ,Point(100,0), self.금액.pSizeORIGEN )
            engine.root.after ( 135 , Animation.SizeChange_FastToSlow ,self.태그, engine, 25 ,Point(100,0), self.태그.pSizeORIGEN )
            engine.root.after ( 180 , Animation.SizeChange_FastToSlow ,self.내용, engine, 20,Point(100,0), self.내용.pSizeORIGEN )
        else:
            engine.root.after ( 410 , self.Visible , False )
            engine.root.after ( 0       , self.Enable , False )
            engine.root.after ( 000 , Animation.SizeChange ,self.큰바, engine, 20 , self.큰바.pSizeORIGEN, Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.창바, engine, 10, self.창바.pSizeORIGEN ,Point(0,400) )
            engine.root.after ( 000 , Animation.SizeChange ,self.작은바, engine, 20 , self.작은바.pSizeORIGEN,Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.설명글, engine, 20 , self.설명글.pSizeORIGEN,Point(0,100) )
            engine.root.after ( 000 , Animation.SizeChange ,self.날자글, engine, 20 , self.날자글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.금액글, engine, 20 , self.금액글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.태그글, engine, 20 , self.태그글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 000 , Animation.SizeChange ,self.내용글, engine, 20 , self.내용글.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.날자, engine, 20 , self.날자.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.금액, engine, 20 , self.금액.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.태그, engine, 20 , self.태그.pSizeORIGEN,Point(100,0) )
            engine.root.after ( 0 , Animation.SizeChange ,self.내용, engine, 20, self.내용.pSizeORIGEN,Point(100,0) )

        return super().Active(start, engine)

class ControlFrame_Graph ( _Frame ):
        """ 컨트롤 박스 프레임중 그래프에 해당되는 프레임입니다."""
        def __init__ ( self ):
            """ 이녀석의 드로우는 engine.g로 하면 안됩니다. 컨트롤 박스의 secondCanvas이용"""
            self.이전 = Object.iButton ( Point(0,0) , Point( 100 , 100 ) , Color.c1 , "컨트롤박스_그래프.이전" , "icon_left.png" )
            self.다음 = Object.iButton ( Point(200,0),Point(100 , 100 ) , Color.c1 , "컨트롤박스_그래프.다음" , "icon_right.png")

        def _Draw(self, g = tkinter.Canvas):
            self.이전.Draw(g)
            self.다음.Draw(g)
        def Start(self, root):
            """ 이벤트들을 등록합니다."""
            self.이전.Start ( root , True )
            self.다음.Start ( root , True )
        def _Enable(self):
            self.이전.enable = self.enable
            self.다음.enable = self.enable
            return super()._Enable()
class ControlFrame_View ( _Frame ):
        """ 컨트롤 박스 프레임중 조회에 해당되는 프레임입니다"""
        def __init__ ( self ):
            """ 이녀석의 드로우는 engine.g로 하면 안됩니다. 컨트롤 박스의 secondCanvas이용"""
            self.다시쓰기 = Object.iButton ( Point(0,0) , Point(100,100) , Color.c1 , "컨트롤박스_조회.다시쓰기" , "icon_rewrite.png" )
            self.찾기 = Object.iButton ( Point ( 100,0) , Point(100,100) , Color.c1 , "컨트롤박스_조회.찾기" , "icon_find.png" )
            self.삭제 = Object.iButton ( Point ( 200,0) , Point(100,100) , Color.c1 , "컨트롤박스_조회.삭제" , "icon_delete.png")
            self.다시쓰기ment = "수정을 하시겠습니까?"
            self.찾기ment = "구현중입니다"
            self.삭제ment = "삭제를 하시겠습니까?"
        def _Draw(self, g = tkinter.Canvas):
            self.다시쓰기.Draw (g)
            self.찾기.Draw ( g )
            self.삭제.Draw( g )
        def Start ( self, root ):
            """ 이벤트들을 등록합니다."""
            self.다시쓰기.Start ( root , True )
            self.찾기.Start ( root , True )
            self.삭제.Start ( root , True )
        def _Enable(self):
            self.다시쓰기.enable = self.enable
            self.찾기.enable = self.enable
            self.삭제.enable = self.enable
            return super()._Enable()
class ControlFrame_Plus ( _Frame ):
        """ 컨트롤 박스중 추가에 해당되는 프레임입니다."""
        def __init__(self):
            """ 이녀석 드로우는 engine.g로 하면 안됨. 꼭 secondCanvas로 받아라"""
            self.새로만들기 = Object.iButton ( Point ( 0 , 0 ) , Point ( 100 , 100 ) , Color.c1 , "컨트롤박스_추가.새로만들기" , "icon_new.png" )
            self.저장 = Object.iButton ( Point ( 100 , 0 ) , Point ( 100 , 100 ) , Color.c1 , "컨트롤박스_추가.저장" , "icon_save.png" )
            self.삭제 = Object.iButton ( Point ( 200 , 0 ) , Point ( 100 , 100 ) , Color.c1 , "컨트롤박스_추가.삭제" , "icon_delete.png" )
            self.새로만들기ment = "새로 만들겠습니까?"
            self.새로만들기에러ment = "수정을 그만두고 새로 만들겠습니까?"
            self.저장ment = "저장을 하시겠습니까?"
            self.저장_다시쓰기ment = "수정 전 데이타는 삭제 되지 않습니다.\n원할 경우 먼저 삭제를 하고 저장하세요.\n삭제하지 않고 저장하겠습니까?"
            self.삭제ment = "수정전 데이타를 삭제하시겠습니까?\n(작성중인 것은 없어지지 않습니다.)"
            self.삭제에러ment = "삭제 할 것이 없습니다.\n조회 항목에서 수정버튼을 눌렀을때 해당됩니다."
            self.삭제완료ment = "삭제가 되었습니다."
            self.취소ment = "데이타 수정이 취소되었습니다.\n(작성중인것은 삭제되고, 데이타는 복원됩니다.)"
        def _Draw(self, g = tkinter.Canvas):
            self.새로만들기.Draw ( g )
            self.저장.Draw ( g )
            self.삭제.Draw ( g )
        def Start ( self , root ):
            """ 이벤트들을 등록합니다 """
            self.새로만들기.Start ( root , True )
            self.저장.Start ( root , True )
            self.삭제.Start ( root , True )
        def _Enable(self):
            self.새로만들기.enable = self.enable
            self.저장.enable = self.enable
            self.삭제.enable = self.enable
            return super()._Enable()
class WarningFrame ( _Frame ):
    def __init__(self ):
        self.창바라인=Object.Box( Point ( 396 , 196 ) , Point ( 608, 308 ) , Color.c4 , "경고창.창바")
        self.창바 = Object.Label ( Point ( 400 , 200 ) , Point ( 600, 300 ) , Color.c2 , "경고창.창바", Text ( "m12버전입니다.",None ) )
        self.제목바 = Object.Label( Point(400 , 200 ) , Point ( 600 , 100 ), Color.c3 , "경고창.제목창" , Text ("알림", None , "24 bold" ) )
        self.확인버튼 = Object.iButton( Point (800 , 400) , Point (100 , 100),Color.c6,"경고창.확인버튼" , "icon_yes.png")
        self.취소버튼 = Object.iButton( Point (900 , 400) , Point (100 , 100),Color.c6,"경고창.취소버튼" , "icon_no.png" )

        self.__sw = 0
    def _Draw(self, g = tkinter.Canvas):
        self.창바라인.Draw(g)
        self.창바.Draw( g )
        self.제목바.Draw(g)
        self.확인버튼.Draw(g)
        self.취소버튼.Draw(g)
    def Start(self, root):
        self.취소버튼.Start( root , True )
        self.확인버튼.Start( root , True )
    def _Enable(self):
        self.취소버튼.enable = self.enable
        self.확인버튼.enable = self.enable
        return super()._Enable()
    def Active(self, start, engine):
        if start == True :
            self.Enable( True )
            self.Visible( True )
            self.AllFrameEnable ( engine )

            self.창바라인.c = Color.c2
            self.취소버튼.c = Color.c2
            self.확인버튼.c = Color.c2
            self.취소버튼.visible = False
            self.확인버튼.visible = False

            engine.root.after ( 0 , Animation.SizeChange , self.창바 , engine , 20 , Point ( 0 , 300 ) , self.창바.pSizeORIGEN )
            engine.root.after ( 0 , Animation.SizeChange , self.창바라인 , engine , 20 , Point ( 0 , 300 ) , self.창바라인.pSizeORIGEN )
            engine.root.after ( 0 , Animation.SizeChange , self.제목바 , engine , 20 , Point ( 0 , 100 ) , self.제목바.pSizeORIGEN )
            engine.root.after ( 0 , Animation.SizeChange , self.창바 , engine , 20 , Point ( 0 , 300 ) , self.창바.pSizeORIGEN )
            engine.root.after ( 450 , self.취소버튼.Visible , True )
            engine.root.after ( 450 , self.확인버튼.Visible , True )
            engine.root.after ( 450 , Animation.ColorChanger , engine , engine.root , Color.c2 , Color.c6 , self.확인버튼, 10 )
            engine.root.after ( 450 , Animation.ColorChanger , engine , engine.root , Color.c2 , Color.c6 , self.취소버튼,10 )
            engine.root.after ( 450 , Animation.ColorChanger , engine , engine.root , Color.c2 , Color.c4 , self.창바라인,10 )
        else:
            engine.root.after ( 0 , Animation.ColorChanger , engine , engine.root , Color.c4 , Color.c2 , self.창바라인,5 )
            engine.root.after ( 0 , Animation.ColorChanger , engine , engine.root , self.취소버튼.c , Color.c2 , self.취소버튼,5 )
            engine.root.after ( 0 , Animation.ColorChanger , engine , engine.root , self.확인버튼.c , Color.c2 , self.확인버튼,5 )
            engine.root.after ( 250 , self.취소버튼.Visible , False )
            engine.root.after ( 250 , self.확인버튼.Visible , False )

            engine.root.after ( 250 , Animation.SizeChange , self.창바 , engine , 20 , self.창바.pSizeORIGEN , Point ( 0 , 300 ) )
            engine.root.after ( 250 , Animation.SizeChange , self.창바라인 , engine , 20 , self.창바라인.pSizeORIGEN , Point ( 0 , 300 ) )
            engine.root.after ( 250 , Animation.SizeChange , self.제목바 , engine , 20 , self.제목바.pSizeORIGEN , Point ( 0 , 100 ) )
            engine.root.after ( 250 , Animation.SizeChange , self.창바 , engine , 20 , self.창바.pSizeORIGEN , Point ( 0 , 300 ) )
            engine.root.after ( 600 , self.Enable , False )
            engine.root.after ( 600 , self.Visible , False )
            engine.root.after ( 600 , self.AllFrameEnable , engine )
        return super().Active(start, engine)
    def AllFrameEnable_SWchanger ( self , intSW ):
        """ 버그잡는 용으로만..."""
        self.__sw = intSW

    def AllFrameEnable ( self , engine ):
        """ 워닝프레임의 고유 기능입니다. 이것은 모든 프레임들의 이벤트들을 끄고 키는 기능이 있습니다."""
        if self.__sw > 0:
            if self.__sw == 1:
                engine.Graph_Frame.Enable ( True )
                engine.Main_Frame.Enable ( True )
                self.__sw = 0
            elif self.__sw == 2:
                engine.View_Frame.Enable ( True )
                engine.Main_Frame.Enable ( True )
                self.__sw = 0
            elif self.__sw == 3:
                engine.Plus_Frame.Enable ( True )
                engine.Main_Frame.Enable ( True )
                self.__sw = 0
            elif self.__sw == 4:
                engine.Main_Frame.Enable ( True )
                self.__sw = 0
            elif self.__sw == 5:
                engine.Plus_Frame.Enable ( True )
                engine.Main_Frame.Enable ( True )
                self.__sw = -1
        elif self.__sw == 0:
            if engine.Warning_Frame.창바.text.text == engine.controlbox.내역.다시쓰기ment:
                engine.Main_Frame.Enable ( False )
                engine.View_Frame.Enable ( False )
                self.__sw = 5
            elif engine.Graph_Frame.enable == True:
                engine.Graph_Frame.Enable()
                engine.Main_Frame.Enable()
                self.__sw = 1
            elif engine.View_Frame.enable == True :
                engine.View_Frame.Enable()
                engine.Main_Frame.Enable()
                self.__sw = 2
            elif engine.Plus_Frame.enable == True :
                engine.Plus_Frame.Enable ( )
                engine.Main_Frame.Enable ( )
                self.__sw = 3 
            else:##이경우는 처음 시작시
                engine.Main_Frame.Enable()
                self.__sw = 4
        else: # selecting은 id.event에서 계속 버튼 누를때 마다 최신화 되고, 조작하진 말자. 데이타 읽기만.
            print ( "=============================================================================, selecting = ", self.selecting )
            if self.selecting ==  2:
                engine.View_Frame.Enable ( False )
                engine.Main_Frame.Enable ( False )
                self.__sw = 2
            elif self.selecting == 1:
                engine.Graph_Frame.Enable ( False )
                engine.Main_Frame.Enable ( False )
                self.__sw = 1