from Point import Point
from Color import Color
from Text import Text
from Graphics import *
import id
class __Rectangle (object):
    """오브젝트를 구성하는데 필요한 것들입니다."""
    def __init__ (self, pStart = Point, pSize = Point, color = Color, id = str):
        self.pStart = pStart
        self.pSize = pSize
        self.pSize보조 = pSize.copy()
        self.pSizeORIGEN = pSize + Point(0,0)
        self.c = color
        self.id = id
class __Data ( __Rectangle ):
    """ """
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str ,text = Text ):
        self.text = text
        return super().__init__(pStart, pSize, color, id)


class __DrawRectangle ( __Rectangle ):
    """데이타를 상속 받고 그래픽을 추가하는 클래스입니다"""
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str):
        super().__init__(pStart, pSize, color, id)
        self.__cOrigen = self.c
        self.visible = True
    def GetOrigenColor ( self ):
        return self.__cOrigen
    def SetOrigenColor ( self , color = Color ):
        self.__cOrigen = color
    def Visible ( self, visible = False ):
        """ visible값을 바꿔줍니다. """
        self.visible = visible
    def Draw ( self, g = tkinter.Canvas ):
        """ Box를 그립니다. """
        if self.visible == True :
            #g.create_rectangle (self.pStart,self.pStart + self.pSize, self.c )
            self._Draw ( g )
    def _Draw ( self, g = tkinter.Canvas ):
        """ tkinter 캔번스 환경에 그립니다. """
        g.create_rectangle ( self.pStart.x , self.pStart.y , self.pSize.x + self.pStart.x , self.pSize.y + self.pStart.y , fill = self.c , width = 0)

class __DrawData ( __DrawRectangle):
    """DrawRectangle을 상속 받고 추가적으로 텍스트 정보를 가집니다"""
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str, text = Text()):
        self.text = text
        return super().__init__(pStart, pSize, color, id)
    def Draw(self, g = tkinter.Canvas):
        """ Box를 Text와 같이 그립니다 """

        super().Draw(g)
        if self.visible == True:
            self.__Draw_Text__ ( g )

    def __Draw_Text__ ( self, g = tkinter.Canvas ):
        if self.text.anchor == None :
            g.create_text ( self.pStart.x + self.pSize.x/2 , self.pStart.y+ self.pSize.y/2  , fill = self.text.c , font = self.text.font , text = self.text.text )
        else :
            g.create_text ( self.pStart.x , self.pStart.y+ self.pSize.y/2 , fill = self.text.c , font = self.text.font , text = self.text.text , anchor = self.text.anchor )

class __Click ( ):
    enable = True
    _Running = False
    def Start ( self,root = tkinter.Canvas ,enable = False ):
        """클릭 이벤트를 작용시킬리면 누르세요"""
        self.enable = enable 
        self.root = root
        if self._Running == False:
            print("이벤트 등록")
            root.bind ( "<Button-1>", self._click, self.id)
            root.bind ( "<ButtonRelease-1>", self._click1, self.id)
            self._Running = True
    def _click ( self, event):
        """enable이 가능한 상태인지 체크 합니다"""
        if self.enable == True :
            self.객체판정(event, False)
    def _click1 ( self, event ):
        if self.enable == True :
            self.객체판정(event, True)
    def 객체판정(self, event, Release):
        """ 직접 프로그래밍 하세요"""
        self.click_event (event, Release)
    def click_event (self , event, Release):
        """직접하세요"""
class __usingICON ( __Rectangle ):
    """ 아이콘을 사용합니다. 아이콘을 출력하는것도 포함됩니다., __init__이 없습니다"""
    _icon = ""
    def setICON ( self , **args ):
        """ 아이콘을 등록합니다. """
        self._icon = tkinter.PhotoImage ( file = args["icon"])
    def getICON ( self ):
        """ 아이콘 파일명을 불러옵니다. """
        return self._icon
    def DrawICON ( self , g = tkinter.Canvas ):
        """ 등록된 아이콘 파일로 드로우 합니다. """
        g.create_image ( self.pStart.x + self.pSize.x/2 , self.pStart.y + self.pSize.y/2 , image = self._icon )

    
class ClickBox ( __Rectangle , __Click ):
    """ 클릭범위만 가지는 박스를 추가시킵니다. 이 박스는 그래픽을 객체를 가지지 않습니다 """
    def __init__(self, pStart = Point, pSize = Point, id = str):

        return super().__init__(pStart, pSize, None, id)
    def 객체판정(self, event, Release):
        if event.x > self.pStart.x and self.pSize.x + self.pStart.x > event.x :
            if event.y > self.pStart.y and self.pSize.y + self.pStart.y > event.y:
                #self.click_event ( event ,Release)
                return super().객체판정(event,Release)

    def click_event(self, event,Release):
        if Release == True :
            id.Event_re ( id = "ClickBoxRelease" , Object = self )
            id.Event_re ( id = self.id, Object = self)
        else:
            id.Event_re ( id = "ClickBox" , Object = self )

class Box ( __DrawRectangle, __Rectangle ):
    """화면에 박스 모양의 오브젝트를 추가합니다"""
    
class Label ( __DrawData , __DrawRectangle , __Rectangle):
    """화면에 라벨을 추가합니다 """
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str, text = Text()):
        return super().__init__(pStart, pSize, color, id, text)

class Button ( __DrawData , __DrawRectangle , __Click, __Rectangle ):
    """화면에 버튼을 추가합니다 """
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str, text = Text()):
        super().__init__(pStart, pSize, color, id, text)

    def 객체판정(self, event, Release):
        if event.x > self.pStart.x and self.pSize.x + self.pStart.x > event.x :
            if event.y > self.pStart.y and self.pSize.y + self.pStart.y > event.y:
                #self.click_event ( event ,Release)
                return super().객체판정(event,Release)

    def click_event(self, event,Release):
        if Release == True :
            id.Event_re( id = self.id, Object = self)
        else:
            id.Event_re( id = "Button", Object = self)
        #return super().click_event(event,Release)
class iButton (  __DrawRectangle , __usingICON,__Click, __Rectangle):
    """ 아이콘을 가지는 버튼을 추가합니다. 텍스트는 없습니다."""
    def __init__(self, pStart = Point, pSize = Point, color = Color, id = str , icon = "fileName"):
        self.setICON ( icon = icon )
        return super().__init__(pStart, pSize, color, id)
    def 객체판정(self, event, Release):
        if event.x > self.pStart.x and self.pSize.x + self.pStart.x > event.x :
            if event.y > self.pStart.y and self.pSize.y + self.pStart.y > event.y:
                #self.click_event ( event ,Release)
                return super().객체판정(event,Release)
    def click_event(self, event,Release):
        print(Release)
        if Release == True :
            id.Event_re( id = self.id, Object = self)
        else:
            id.Event_re( id = "Button", Object = self)
    def Draw(self, g = tkinter.Canvas):
        super().Draw(g)
        if self.visible == True:
            self.DrawICON ( g )

class TextOnlyButton ( Button , __DrawData, __DrawRectangle, __Click, __Rectangle ):
    """ 택스트만 출력하는 버튼을 만듬"""
    def __init__(self, pStart = Point, pSize = Point, id = str, text = Text()):
        return super().__init__(pStart, pSize, text.c, id, text)
    def Draw(self, g = tkinter.Canvas):
        if self.visible == True:
            self.__Draw_Text__( g )
    def click_event(self, event, Release):
        if Release == True :
            id.Event_re( id = "TextClickRelease", Object = self)
            id.Event_re( id = self.id , Object = self)
        else:
            id.Event_re( id = "TextClick", Object = self)

class MenuList ( ):
    """메뉴리스트를 만듭니다. 거대한 상자를 그리고 라벨들을 만듭니다. 내장된 오브젝트들은 리스트 자료형으로 관리하세요"""
    def __init__ ( self, start = Point , size = Point , color = Color , subColor = Color , id = "" ):
        """ size.y / 100 한만큼 필요한 요소들이 자동 생성 됩니다. 이 값은 bxMain이 그대로 상속 받습니다."""
        self.lbTitle = []
        self.lbSub = []
        self.cbClickBox = []
        self.bxMain = Box( start , size , color, id + ".메인박스" )
        self.rightBar = Box( Point ( 0, start.y ) , Point ( start.x , 100 ) , subColor , id + ".오른쪽바" )
        self.liftBar = Box ( Point ( start.x + size.x , start.y ), Point ( 1400 - start.x - size.x, 100 ) , subColor , id + ".왼쪽바" )
        self.visible = False
        self.enable = False

        num = int ( size.y / 100 )
        i = 0
        while i < num :
            #
            # 아이디들은 "메뉴id.항목이름"+"숫자"
            #
            self.lbTitle.append ( Label ( Point ( start.x , start.y + 100 * i ), Point( 100 , 100 ) , None , id + ".제목" + i , None ) )
            self.lbSub.append ( Label ( Point ( start.x + 100 ,start.y + 100 * i ), Point( size.x - 100 ,100 ) , None , id + ".서브" + i , None ) )
            self.cbClickBox.append ( ClickBox ( Point ( start.x , start.y + 100 * i ), Point( size.x , 100 ) , id + ".클릭" + i  ) )
            i = i + 1
    def Draw ( self , g = tkinter.Canvas ):
        """리스트 안의 모든 요소들을 그립니다"""
    def start ( self ):
        """모든 이벤트를 동작 시킵니다"""
