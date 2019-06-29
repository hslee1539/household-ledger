import Color
import Animation
from Point import Point

#만든 목적: 굳이 Object.py에 있는 click클레스에 하지 않고
#           따로 id를 만들어 이벤트 처리 하는 이유는
#           이벤트 처리할때 객체들 간의 구별해주기 위해서임
#           이렇게 하면 class MainButton ( Button) , class PlusButton(Button)식으로
#           비슷한 의미의 클래스를 따로 만들지 않고
#           객체로 여러개 만들어 처리해주기 위함임
#   
#호출 되는 경우:   Object.py에서 버튼을 클릭했을때 기본적으로 Button과 ButtonRelease가 나오고
#                  해당 객체의 범위 내에서 선택을 할 경우 객체.id가 Event_re.id로 받아진다


# 클래스 원칙중 단일 책임 원칙을 많이 어김....
# 
# 나중에 꼭 수정하자!!!!
#
#
def id_Start ( ):
    """ 시작시 이것도 같이 호출해야 합니다. 없어도 지장은 없지만, 잔버그를 고칠수 있습니다. """
    _ViewPage ( )

def _ViewPage ( ):
    engine.ThreadStart()
    datas = engine.data.MakeList()
    engine.View_Frame.이전글.text.text = datas[0]
    engine.View_Frame.다음글.text.text = datas[2]
    engine.View_Frame.날자글.text.text = datas[1]["날자"]
    engine.View_Frame.금액글.text.text = datas[1]["금액"]
    engine.View_Frame.태그글.text.text = datas[1]["태그"]
    engine.View_Frame.내용글.text.text = datas[1]["내용"]
    engine.ThreadEnd()

selected = 0
def _Closer ( selecting ):
    engine.Warning_Frame.selecting = selecting
    global selected
    if selected == 1:
        engine.root.after ( 0 , engine.Graph_Frame.Active, False , engine )
    elif selected == 2:
        engine.root.after ( 0 , engine.View_Frame.Active, False , engine)
    elif selected == 3:
        engine.root.after ( 0 , engine.Plus_Frame.Active , False , engine)

    if selected > 0:
        if selecting == 1 :
            engine.root.after ( 500 , engine.Graph_Frame.WaitActive, True , engine)
        if selecting == 2 :
            if selected == 1:
                engine.root.after ( 1400 , engine.View_Frame.WaitActive, True , engine) # 그래프 프레임이 길기 때문에
            else:
                engine.root.after ( 500 , engine.View_Frame.WaitActive, True , engine)
        if selecting == 3:
            if selected == 1:
                engine.root.after ( 1400 , engine.Plus_Frame.WaitActive , True , engine) # 그래프 프레임이 길기 때문에
            else:
                engine.root.after ( 500 , engine.Plus_Frame.WaitActive , True , engine)
        if selecting == 4:
            engine.root.after ( 0 , engine.Main_Frame.Active, False , engine)
            engine.root.after ( 3500 , engine.root.destroy )
    else:
        if selecting == 1 :
            engine.root.after ( 0 , engine.Graph_Frame.WaitActive, True , engine)
        if selecting == 2 :
            engine.root.after ( 0 , engine.View_Frame.WaitActive, True , engine)
        if selecting == 3 :
            engine.root.after ( 0 , engine.Plus_Frame.WaitActive , True , engine)
        if selecting == 4 :
            engine.root.after ( 0 , engine.Main_Frame.WaitActive, False , engine)
            engine.root.after ( 3500 , engine.root.destroy )
    selected = selecting
def _ButtonLock ():
    """Tk.after는 사전형 매개변수를 못집어 넣어 이것으로 대신 하세요"""
    Event_re ( id = "ButtonLock")

def Event_re ( **args ):
    """ 새롭게 다시 만든 이벤트입니다. 매개변수를 사전형으로 받아 드리립니다. 따라서 여러가지 인수를 추가적으로 여기서 기역할 필요 없음"""
    print( " Start , MainFrame.enable = ",engine.Main_Frame.enable )
    try:
        id = args["id"]
        Object = args["Object"]
    except:
        id = args["id"]
    print("----Event_re")

    if id == "Button":# 클릭시 파란색 이팩트 
        print(Object)
        #Object.c = Color.Color.c4
        Color.ColorChanger ( engine ,engine.root , Object.c , Color.Color.c4, Object , 3 )
        Event_re ( id = "DrawAll" )
    elif id == "ButtonRelease":# 원래 색으로 돌아옴
        Color.ColorChanger ( engine ,engine.root , Object.c , Object.GetOrigenColor() , Object , 10 )
        Event_re ( id = "DrawMainFrame" )
    elif id == "DrawMainFrame":
        engine.Main_Frame.Draw( g )
    elif id == "ButtonLock":
        if engine.Main_Frame.enable == True:
            engine.Main_Frame.Enable( False )
        else:
            engine.Main_Frame.Enable( True )
    elif id[0:8] == "ClickBox":
        if id == "ClickBox":
            engine.ThreadStart ()
            if args["Object"].id[0:2] == engine.View_Frame.날자범위.id[0:2]:
                if args["Object"].id == engine.View_Frame.날자범위.id:
                    engine.View_Frame.날자.text.FontSize ( int( engine.View_Frame.날자.text.FontSize() ) - 5 )
                    engine.View_Frame.날자글.text.FontSize ( int( engine.View_Frame.날자글.text.FontSize() ) - 5 )
                elif args["Object"].id == engine.View_Frame.금액범위.id:
                    engine.View_Frame.금액.text.FontSize ( int ( engine.View_Frame.금액.text.FontSize() ) - 5 )
                    engine.View_Frame.금액글.text.FontSize(int ( engine.View_Frame.금액글.text.FontSize () ) -5 )
                elif args["Object"].id == engine.View_Frame.태그범위.id:
                    engine.View_Frame.태그.text.FontSize ( int ( engine.View_Frame.태그.text.FontSize () ) - 5 )
                    engine.View_Frame.태그글.text.FontSize(int( engine.View_Frame.태그글.text.FontSize()) - 5 )
                elif args["Object"].id == engine.View_Frame.내용범위.id:
                    engine.View_Frame.내용.text.FontSize ( int ( engine.View_Frame.내용.text.FontSize () ) - 5 )
                    engine.View_Frame.내용글.text.FontSize(int ( engine.View_Frame.내용글.text.FontSize())- 5 )
            else:
                if args["Object"].id == engine.Plus_Frame.날자범위.id:
                    engine.Plus_Frame.날자.text.FontSize ( int ( engine.Plus_Frame.날자.text.FontSize () ) - 5 )
                    engine.Plus_Frame.날자글.text.FontSize(int( engine.Plus_Frame.날자글.text.FontSize()) - 5 )
                elif args["Object"].id == engine.Plus_Frame.금액범위.id :
                    engine.Plus_Frame.금액.text.FontSize ( int ( engine.Plus_Frame.금액.text.FontSize() ) - 5 )
                    engine.Plus_Frame.금액글.text.FontSize(int( engine.Plus_Frame.금액글.text.FontSize())- 5 )
                elif args["Object"].id == engine.Plus_Frame.태그범위.id:
                    engine.Plus_Frame.태그.text.FontSize ( int ( engine.Plus_Frame.태그.text.FontSize () ) - 5 )
                    engine.Plus_Frame.태그글.text.FontSize(int ( engine.Plus_Frame.태그글.text.FontSize())- 5 )
                elif args["Object"].id == engine.Plus_Frame.내용범위.id:
                    engine.Plus_Frame.내용.text.FontSize ( int ( engine.Plus_Frame.내용.text.FontSize () ) - 5 )
                    engine.Plus_Frame.내용글.text.FontSize(int( engine.Plus_Frame.내용글.text.FontSize()) - 5 )
        else:
            if args["Object"].id[0:2] == engine.View_Frame.날자범위.id[0:2]:
                if args["Object"].id == engine.View_Frame.날자범위.id:
                    Animation.FontSize ( engine.View_Frame.날자 , engine, 5 , int ( engine.View_Frame.날자.text.FontSize() ) , int ( engine.View_Frame.날자.text.FontSize ( ) ) + 5 )
                    Animation.FontSize ( engine.View_Frame.날자글 , engine, 5 , int ( engine.View_Frame.날자글.text.FontSize() ) , int ( engine.View_Frame.날자글.text.FontSize ( ) ) + 5 )
                elif args["Object"].id == engine.View_Frame.금액범위.id:
                    Animation.FontSize ( engine.View_Frame.금액 , engine, 5 , int ( engine.View_Frame.금액.text.FontSize () ) , int ( engine.View_Frame.금액.text.FontSize ( ) ) + 5 )
                    Animation.FontSize ( engine.View_Frame.금액글, engine,5, int ( engine.View_Frame.금액글.text.FontSize()) , int ( engine.View_Frame.금액글.text.FontSize()) + 5 )
                elif args["Object"].id == engine.View_Frame.태그범위.id:
                    Animation.FontSize ( engine.View_Frame.태그 , engine , 5 , int ( engine.View_Frame.태그.text.FontSize ( ) ) , int ( engine.View_Frame.태그.text.FontSize() ) + 5)
                    Animation.FontSize ( engine.View_Frame.태그글,engine , 5, int ( engine.View_Frame.태그글.text.FontSize() ) , int ( engine.View_Frame.태그글.text.FontSize())+ 5)
                elif args["Object"].id == engine.View_Frame.내용범위.id:
                    Animation.FontSize ( engine.View_Frame.내용 , engine , 5 , int ( engine.View_Frame.내용.text.FontSize () ) , int ( engine.View_Frame.내용.text.FontSize ( ) ) + 5 )
                    Animation.FontSize ( engine.View_Frame.내용글,engine , 5 , int ( engine.View_Frame.내용글.text.FontSize()),int ( engine.View_Frame.내용글.text.FontSize() ) + 5 )
            else:
                if args["Object"].id == engine.Plus_Frame.날자범위.id:
                    Animation.FontSize ( engine.Plus_Frame.날자 , engine , 5 , int ( engine.Plus_Frame.날자.text.FontSize ( ) ) , int ( engine.Plus_Frame.날자.text.FontSize ( ) ) + 5 )
                    Animation.FontSize ( engine.Plus_Frame.날자글 , engine,5, int ( engine.Plus_Frame.날자글.text.FontSize()) , int ( engine.Plus_Frame.날자글.text.FontSize() ) + 5 )
                elif args["Object"].id == engine.Plus_Frame.금액범위.id:
                    Animation.FontSize ( engine.Plus_Frame.금액 , engine , 5 , int ( engine.Plus_Frame.금액.text.FontSize ( ) ) , int ( engine.Plus_Frame.금액.text.FontSize () )  + 5 )
                    Animation.FontSize ( engine.Plus_Frame.금액글,engine, 5 , int ( engine.Plus_Frame.금액글.text.FontSize() ) , int ( engine.Plus_Frame.금액글.text.FontSize()) + 5 )
                elif args["Object"].id == engine.Plus_Frame.태그범위.id:
                    Animation.FontSize ( engine.Plus_Frame.태그 , engine , 5 , int ( engine.Plus_Frame.태그.text.FontSize ( ) ) , int ( engine.Plus_Frame.태그.text.FontSize () ) + 5 )
                    Animation.FontSize ( engine.Plus_Frame.태그글,engine , 5, int ( engine.Plus_Frame.태그글.text.FontSize() ) , int ( engine.Plus_Frame.태그글.text.FontSize()) + 5 )
                elif args["Object"].id == engine.Plus_Frame.내용범위.id:
                    Animation.FontSize ( engine.Plus_Frame.내용 , engine , 5 , int ( engine.Plus_Frame.내용.text.FontSize ( ) ) , int ( engine.Plus_Frame.내용.text.FontSize ( ) ) + 5 )
                    Animation.FontSize ( engine.Plus_Frame.내용글,engine, 5 , int ( engine.Plus_Frame.내용글.text.FontSize() ) , int ( engine.Plus_Frame.내용글.text.FontSize() ) + 5 )



        engine.ThreadEnd ()
    elif id == "TextClick":
        engine.ThreadStart ()
        args["Object"].text.FontSize ( int(args["Object"].text.FontSize()) -5 )
        engine.ThreadEnd ()
    elif id == "TextClickRelease":
        Animation.FontSize ( args["Object"] , engine , 5 , int ( args["Object"].text.FontSize () )  , int ( args["Object"].text.FontSize ( ) ) + 5 )
    elif id == "MakeGraph":
        data = engine.data.sumsameList ( "태그" )
        data = engine.data.tool.percentData ( data )
        if len( data ) > 0 and data[0]["금액"] < 0:
            engine.Graph_Frame.첫이름.text.text = data[0]["태그"] + "\n" + str(-data[0]["금액"]) + "%"
            engine.Graph_Frame.첫그래프.pSize보조.y = ( data[0]["금액"]/100 + 1 )* engine.Graph_Frame.첫그래프.pSizeORIGEN.y
        if len( data ) > 1 and data[1]["금액"] < 0:
            engine.Graph_Frame.둘이름.text.text = data[1]["태그"] + "\n" + str(-data[1]["금액"]) + "%"
            engine.Graph_Frame.둘그래프.pSize보조.y = ( data[1]["금액"]/100 + 1 )* engine.Graph_Frame.둘그래프.pSizeORIGEN.y
        if len( data ) > 2 and data[2]["금액"] < 0:
            engine.Graph_Frame.삼이름.text.text = data[2]["태그"] + "\n" + str(-data[2]["금액"]) + "%"
            engine.Graph_Frame.삼그래프.pSize보조.y = ( data[2]["금액"]/100 + 1 )* engine.Graph_Frame.삼그래프.pSizeORIGEN.y
        if len( data ) > 3 and data[3]["금액"] < 0:
            engine.Graph_Frame.넷이름.text.text = data[3]["태그"] + "\n" + str(-data[3]["금액"]) + "%"
            engine.Graph_Frame.넷그래프.pSize보조.y = ( data[3]["금액"]/100 + 1 )* engine.Graph_Frame.넷그래프.pSizeORIGEN.y
        if len( data ) > 4 and data[4]["금액"] < 0:
            engine.Graph_Frame.오이름.text.text = data[4]["태그"] + "\n" + str(-data[4]["금액"]) + "%"
            engine.Graph_Frame.오그래프.pSize보조.y = ( data[4]["금액"]/100 + 1 )* engine.Graph_Frame.오그래프.pSizeORIGEN.y
        if len( data ) > 0:
            지출 = engine.data.tool.plusData ( data, False )
            engine.Graph_Frame.전체이름.text.text = "전체\n" + str (-지출) + "%"
            engine.Graph_Frame.전체그래프.pSize보조.y = ( 지출/100 + 1 )* engine.Graph_Frame.전체그래프.pSizeORIGEN.y
    elif id == "PlusData":
        error = engine.data.PlusData ( 날자 = engine.Plus_Frame.날자글.text.text,
                                      금액 = engine.Plus_Frame.금액글.text.text,
                                      태그 = engine.Plus_Frame.태그글.text.text,
                                      내용 = engine.Plus_Frame.내용글.text.text)
        if error == "성공":
            Event_re ( id = "MakeGraph" ) # 그래프 최신화
            Color.ColorChanger ( engine , engine.root , Color.Color.c4,Color.Color.c3 , engine.Plus_Frame.큰바 , 20 )
            selected = int ( (engine.Plus_Frame.작은바.pStart.y - engine.Plus_Frame.창바.pStart.y) / 100 )
            engine.Plus_Frame.날자글.text.text = ""
            engine.Plus_Frame.금액글.text.text = ""
            engine.Plus_Frame.태그글.text.text = ""
            engine.Plus_Frame.내용글.text.text = ""
            engine.Plus_Frame.설명글.text.text = "저장이 되었습니다."
            if selected == 0: # 조회 항목이 보고 있는 것으로 업데이트
                id = "날자"
            elif selected == 1:
                id = "금액"
            elif selected == 2:
                id = "태그"
            elif selected == 3:
                id = "내용"
            engine.data.MakeViewData( "날자" )
            engine.Warning_Frame.창바.text.text = "" # 버튼 클릭으로 했을때, 저장했으므로 다시 쓰기 상태가 풀려야 함
        elif error[0:2] == "날자":
            engine.Plus_Frame.설명글.text.text = error
            Color.ColorChanger ( engine , engine.root , Color.Color.c2,Color.Color.c3 , engine.Plus_Frame.작은바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c3,Color.Color.c2 , engine.Plus_Frame.큰바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c2 , engine.Plus_Frame.창바 , 20 )
            Animation.Move ( engine.Plus_Frame.큰바 , engine , 20 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 300 ) )
            Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 300 ) )
            Animation.Move ( engine.Plus_Frame.설명글 , engine , 25 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 300 ) )
        elif error[0:2] == "금액":
            Color.ColorChanger ( engine , engine.root , Color.Color.c2,Color.Color.c3 , engine.Plus_Frame.작은바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c3,Color.Color.c2 , engine.Plus_Frame.큰바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c2 , engine.Plus_Frame.창바 , 20 )
            engine.Plus_Frame.설명글.text.text = error
            Animation.Move ( engine.Plus_Frame.큰바 , engine , 20 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 400 ) )
            Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 400 ) )
            Animation.Move ( engine.Plus_Frame.설명글 , engine , 25 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 400 ) )
        elif error[0:2] == "태그":
            Color.ColorChanger ( engine , engine.root , Color.Color.c2,Color.Color.c3 , engine.Plus_Frame.작은바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c3,Color.Color.c2 , engine.Plus_Frame.큰바 , 20 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c2 , engine.Plus_Frame.창바 , 20 )
            engine.Plus_Frame.설명글.text.text = error
            Animation.Move ( engine.Plus_Frame.큰바 , engine , 20 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 500 ) )
            Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 500 ) )
            Animation.Move ( engine.Plus_Frame.설명글 , engine , 25 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 500 ) )
    elif id == "KeyEvent":
        if engine.Plus_Frame.enable == True:
            engine.ThreadStart( )
            print("실행된 char = ", args["char"])
            selected = int ( (engine.Plus_Frame.작은바.pStart.y - engine.Plus_Frame.창바.pStart.y) / 100 )
            args["char"] = engine.event.Tool.Filter ( args["char"] , int(selected/2) )
            if selected == 0:

                if args["char"] != "Eraser":
                    if args["char"] != "Enter":
                        if args["char"] != "Tab" and args["char"] != "Space":
                            engine.Plus_Frame.날자글.text.text = engine.Plus_Frame.날자글.text.text + args["char"]
                        else:
                            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                            Event_re( id = "추가.금액범위" )
                    else:
                        Event_re( id = "PlusData" )
                else:
                    Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 5 )
                    engine.Plus_Frame.날자글.text.text = engine.Plus_Frame.날자글.text.text[ 0 : len(engine.Plus_Frame.날자글.text.text) - 1 ]
            elif selected == 1:
                if args["char"] != "Eraser":
                    if args["char"] != "Enter":
                        if args["char"] != "Tab":
                            if args["char"] != "Space":
                                if engine.Plus_Frame.금액글.text.text == "":##아무것도 없을 경우 +를 추가합니다.
                                    Color.ColorChanger ( engine , engine.root , Color.Color.c4,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                                    engine.Plus_Frame.금액글.text.text = "+"
                                engine.Plus_Frame.금액글.text.text = engine.Plus_Frame.금액글.text.text + args["char"]
                            else:
                                if engine.Plus_Frame.금액글.text.text[0:1] == "+":
                                    Color.ColorChanger ( engine , engine.root , Color.Color.c4,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                                    engine.Plus_Frame.금액글.text.text = "-" + engine.Plus_Frame.금액글.text.text[1:]
                                else:
                                    Color.ColorChanger ( engine , engine.root , Color.Color.c4,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                                    engine.Plus_Frame.금액글.text.text = "+" + engine.Plus_Frame.금액글.text.text[1:]
                        else:
                            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                            Event_re( id = "추가.태그범위" )
                    else:
                        Event_re( id = "PlusData" )
                else:
                    Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 5 )
                    engine.Plus_Frame.금액글.text.text = engine.Plus_Frame.금액글.text.text[ 0 : 1] +engine.Plus_Frame.금액글.text.text[ 1 : len(engine.Plus_Frame.금액글.text.text) - 1 ]
            elif selected == 2:
                if args["char"] != "Eraser":
                    if args["char"] != "Enter":
                        if args["char"] != "Tab":
                            if args["char"] != "Space":
                                if engine.Plus_Frame.태그글.text.text == "":##아무것도 없을 경우 +를 추가합니다.
                                    engine.Plus_Frame.태그글.text.text = "#"
                                engine.Plus_Frame.태그글.text.text = engine.Plus_Frame.태그글.text.text + args["char"]
                            else:
                                if engine.Plus_Frame.태그글.text.text[0:1] == "#":
                                    engine.Plus_Frame.태그글.text.text = engine.Plus_Frame.태그글.text.text[1:]
                                else:
                                    engine.Plus_Frame.태그글.text.text = "#" + engine.Plus_Frame.태그글.text.text
                        else:
                            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                            Event_re( id = "추가.내용범위" )
                    else:
                        Event_re( id = "PlusData" )
                else:
                    Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 5 )
                    engine.Plus_Frame.태그글.text.text = engine.Plus_Frame.태그글.text.text[ 0 : len(engine.Plus_Frame.태그글.text.text) - 1 ]
            elif selected == 3:
                if args["char"] != "Eraser":
                    if args["char"] != "Enter":
                        if args["char"] != "Tab":
                            if args["char"] != "Space":
                                engine.Plus_Frame.내용글.text.text = engine.Plus_Frame.내용글.text.text + args["char"]
                            else:
                                engine.Plus_Frame.내용글.text.text = engine.Plus_Frame.내용글.text.text + " "
                        else:
                            Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 15 )
                            Event_re( id = "추가.날자범위" )
                    else:
                        Event_re( id = "PlusData" )
                else:
                    Color.ColorChanger ( engine , engine.root , Color.Color.c6,Color.Color.c3 , engine.Plus_Frame.작은바 , 5 )
                    engine.Plus_Frame.내용글.text.text = engine.Plus_Frame.내용글.text.text[ 0 : len(engine.Plus_Frame.내용글.text.text) - 1 ]
            engine.ThreadEnd()
            print("selected = ", selected)


           
    elif id == engine.Main_Frame.메인.id:
        Event_re ( id = "ButtonLock" )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.메인.c , Color.Color.c3 , engine.Main_Frame.메인 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.내역.c , Color.Color.c6 , engine.Main_Frame.내역 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.추가.c , Color.Color.c6 , engine.Main_Frame.추가 , 10 )
        engine.root.after ( 3000 , _ButtonLock )
        _Closer ( 1 )
        if engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment or engine.Warning_Frame.창바.text.text ==  engine.controlbox.내역.다시쓰기ment:
            engine.Warning_Frame.창바.text.text = engine.controlbox.추가.취소ment
            engine.Warning_Frame.Active( True , engine )
    elif id == engine.Main_Frame.내역.id:
        Event_re ( id = "ButtonLock" )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.내역.c , Color.Color.c3 , engine.Main_Frame.내역 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.메인.c , Color.Color.c6 , engine.Main_Frame.메인 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.추가.c , Color.Color.c6 , engine.Main_Frame.추가 , 10 )
        engine.root.after ( 3000 , _ButtonLock )
        _Closer ( 2 )
        if engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment or engine.Warning_Frame.창바.text.text ==  engine.controlbox.내역.다시쓰기ment:
            engine.Warning_Frame.창바.text.text = engine.controlbox.추가.취소ment
            engine.Warning_Frame.Active( True , engine )
    elif id == engine.Main_Frame.추가.id:
        Event_re ( id = "ButtonLock" )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.추가.c , Color.Color.c3 , engine.Main_Frame.추가 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.메인.c , Color.Color.c6 , engine.Main_Frame.메인 , 10 )
        Color.ColorChanger ( engine , engine.root , engine.Main_Frame.내역.c , Color.Color.c6 , engine.Main_Frame.내역 , 10 )
        engine.root.after ( 3000 , _ButtonLock )
        _Closer ( 3 )
        
    elif id == "내역.이전글":
        if engine.View_Frame.이전글.text.text != '   ':
            engine.View_Frame.창바.c
            engine.View_Frame.큰바.c
            engine.View_Frame.작은바.c
            #Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c2 , engine.View_Frame.창바 , 2 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c2 , engine.View_Frame.큰바 , 4 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c3 , engine.View_Frame.작은바,6 )

        engine.data.PageDown( )
        _ViewPage()
    elif id == "내역.다음글":
        if engine.View_Frame.다음글.text.text != "   ": 
            engine.View_Frame.창바.c
            engine.View_Frame.큰바.c
            engine.View_Frame.작은바.c
            #Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c2 , engine.View_Frame.창바 , 2 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c2 , engine.View_Frame.큰바 , 4 )
            Color.ColorChanger ( engine , engine.root , Color.Color.c6 , Color.Color.c3 , engine.View_Frame.작은바,6 )
        engine.data.PageUp( )
        _ViewPage()
    elif id == "내역.날자범위":
        Animation.Move ( engine.View_Frame.다음글 , engine , 15 , engine.View_Frame.다음글.pStart , Point (1200,300) )
        Animation.Move ( engine.View_Frame.이전글 , engine , 15 , engine.View_Frame.이전글.pStart , Point (0,300) )
        Animation.Move ( engine.View_Frame.큰바 , engine , 15 , engine.View_Frame.큰바.pStart , Point (0,300) )
        Animation.Move ( engine.View_Frame.작은바 , engine , 15 , engine.View_Frame.작은바.pStart , Point (500,300) )
        engine.data.MakeViewData( "날자" )
        _ViewPage()
    elif id == "내역.금액범위":
        Animation.Move ( engine.View_Frame.다음글 , engine , 15 , engine.View_Frame.다음글.pStart , Point (1200,400) )
        Animation.Move ( engine.View_Frame.이전글 , engine , 15 , engine.View_Frame.이전글.pStart , Point (0,400) )
        Animation.Move ( engine.View_Frame.큰바 , engine , 15 , engine.View_Frame.큰바.pStart , Point (0,400) )
        Animation.Move ( engine.View_Frame.작은바 , engine , 15 , engine.View_Frame.작은바.pStart , Point (500,400) )
        engine.data.MakeViewData( "금액" )
        _ViewPage()
    elif id == "내역.태그범위":
        Animation.Move ( engine.View_Frame.다음글 , engine , 15 , engine.View_Frame.다음글.pStart , Point (1200,500) )
        Animation.Move ( engine.View_Frame.이전글 , engine , 15 , engine.View_Frame.이전글.pStart , Point (0,500) )
        Animation.Move ( engine.View_Frame.큰바 , engine , 15 , engine.View_Frame.큰바.pStart , Point (0,500) )
        Animation.Move ( engine.View_Frame.작은바 , engine , 15 , engine.View_Frame.작은바.pStart , Point (500,500) )
        engine.data.MakeViewData( "태그" )
        _ViewPage()
    elif id == "내역.내용범위":
        Animation.Move ( engine.View_Frame.다음글 , engine , 15 , engine.View_Frame.다음글.pStart , Point (1200,600) )
        Animation.Move ( engine.View_Frame.이전글 , engine , 15 , engine.View_Frame.이전글.pStart , Point (0,600) )
        Animation.Move ( engine.View_Frame.큰바 , engine , 15 , engine.View_Frame.큰바.pStart , Point (0,600) )
        Animation.Move ( engine.View_Frame.작은바 , engine , 15 , engine.View_Frame.작은바.pStart , Point (500,600) )
        engine.data.MakeViewData( "내용" )
        _ViewPage()
    elif id == "추가.날자범위":
        engine.Plus_Frame.설명글.text.text = "8글자를 입력하세요!"
        Animation.Move ( engine.Plus_Frame.큰바 , engine , 15 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 300 ) )
        Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 300 ) )
        Animation.Move ( engine.Plus_Frame.설명글 , engine , 15 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 300 ) )
    elif id == "추가.금액범위":
        engine.Plus_Frame.설명글.text.text = "스페이스바로 금액이 +,-를 설정할수 있어요!"
        Animation.Move ( engine.Plus_Frame.큰바 , engine , 15 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 400 ) )
        Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 400 ) )
        Animation.Move ( engine.Plus_Frame.설명글 , engine , 15 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 400 ) )
    elif id == "추가.태그범위":
        engine.Plus_Frame.설명글.text.text = "4글자 이내로 입력하세요!"
        Animation.Move ( engine.Plus_Frame.큰바 , engine , 15 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 500 ) )
        Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 500 ) )
        Animation.Move ( engine.Plus_Frame.설명글 , engine , 15 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 500 ) )
    elif id == "추가.내용범위":
        engine.Plus_Frame.설명글.text.text = "자유롭게 입력하세요!"
        Animation.Move ( engine.Plus_Frame.큰바 , engine , 15 , engine.Plus_Frame.큰바.pStart , Point ( 0 , 600 ) )
        Animation.Move ( engine.Plus_Frame.작은바 , engine , 15 , engine.Plus_Frame.작은바.pStart , Point ( 600 , 600 ) )
        Animation.Move ( engine.Plus_Frame.설명글 , engine , 15 , engine.Plus_Frame.설명글.pStart , Point ( 0 , 600 ) )    
    elif id == "메인.종료": # 4
        Event_re ( id = "ButtonLock" )
        engine.root.after ( 1600 , _ButtonLock )
        _Closer ( 4 )
        #컨트롤박스_조회.다시쓰기
    elif id[0:5] == "컨트롤박스":
        Color.ColorChanger ( engine , engine.root , Color.Color.c4 , Color.Color.c1 , args["Object"] , 10 )
        engine.root.after ( 400 , engine.controlbox.AnimationUp )
        if id[6:8] == "조회":
            if id[9:] == "다시쓰기":
                print("다시쓰기를 클릭함")
                engine.Warning_Frame.창바.text.text = engine.controlbox.내역.다시쓰기ment
                engine.Warning_Frame.Active( True , engine )
            elif id[9:] == "찾기":
                engine.Warning_Frame.창바.text.text = engine.controlbox.내역.찾기ment
                engine.Warning_Frame.Active( True , engine )
            elif id[9:] == "삭제":
                engine.Warning_Frame.창바.text.text = engine.controlbox.내역.삭제ment
                engine.Warning_Frame.Active( True , engine )
        elif id[6:8] == "추가":# 내역에서 넘오는 경우가 있어 조금 김
            if id[9:] == "삭제":
                if engine.Warning_Frame.창바.text.text == engine.controlbox.내역.다시쓰기ment: # 내역에서 다시쓰기로 넘어온 경우가 있으므로
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.삭제ment
                    engine.Warning_Frame.Active( True , engine )
                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment:
                    engine.Warning_Frame.Active( True , engine )

                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment:# 새로 만들기가 넘어운 경우로 받았을때
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.삭제ment
                    engine.Warning_Frame.Active( True , engine )
                else:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.삭제에러ment

                    engine.Warning_Frame.Active( True , engine )
            elif id[9:] == "새로만들기":
                if engine.Warning_Frame.창바.text.text == engine.controlbox.내역.다시쓰기ment: # 내역에서 다시쓰기로 넘어온 경우때문에
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.새로만들기에러ment
                    engine.Warning_Frame.Active( True , engine )
                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment:
                    engine.Warning_Frame.Active( True , engine )
                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.새로만들기에러ment
                    engine.Warning_Frame.Active( True , engine )
                else:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.새로만들기ment
                    engine.Warning_Frame.Active( True , engine )
            elif id[9:] == "저장":
                if engine.Warning_Frame.창바.text.text == engine.controlbox.내역.다시쓰기ment:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.저장_다시쓰기ment
                    engine.Warning_Frame.Active( True , engine )
                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment:
                    engine.Warning_Frame.Active ( True , engine )
                elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.저장_다시쓰기ment
                    engine.Warning_Frame.Active( True , engine )
                else:
                    engine.Warning_Frame.창바.text.text = engine.controlbox.추가.저장ment
                    engine.Warning_Frame.Active( True , engine )

        else:
            engine.Warning_Frame.창바.text.text = "구현중입니다."
            engine.Warning_Frame.Active( True , engine )
    elif id[0:3] == "경고창":
        engine.Warning_Frame.Active( False , engine )
        engine.Warning_Frame.Enable ( False )
        if engine.Warning_Frame.창바.text.text == engine.start_ment: ### 시작시 나오는 알림창 선택시
            Event_re ( id = "MakeGraph" )
        elif id[4:] == "확인버튼":
            if engine.Warning_Frame.창바.text.text == engine.controlbox.내역.삭제ment:
                engine.data.delete()
                engine.data.reMakeViewData()
                engine.data.MakeList()
                _ViewPage()
            elif engine.Warning_Frame.창바.text.text == engine.controlbox.내역.다시쓰기ment:
                engine.Plus_Frame.날자글.text.text = str(engine.View_Frame.날자글.text.text)
                engine.Plus_Frame.금액글.text.text = str(engine.View_Frame.금액글.text.text)
                engine.Plus_Frame.태그글.text.text = engine.View_Frame.태그글.text.text
                engine.Plus_Frame.내용글.text.text = engine.View_Frame.내용글.text.text
                
                Color.ColorChanger ( engine , engine.root , engine.Main_Frame.추가.c , Color.Color.c3 , engine.Main_Frame.추가 , 10 )
                Color.ColorChanger ( engine , engine.root , engine.Main_Frame.메인.c , Color.Color.c6 , engine.Main_Frame.메인 , 10 )
                Color.ColorChanger ( engine , engine.root , engine.Main_Frame.내역.c , Color.Color.c6 , engine.Main_Frame.내역 , 10 )
                _Closer ( 3 )

            elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기ment:
                engine.Plus_Frame.날자글.text.text = ""
                engine.Plus_Frame.금액글.text.text = ""
                engine.Plus_Frame.태그글.text.text = ""
                engine.Plus_Frame.내용글.text.text = ""
                engine.Warning_Frame.창바.text.text = ""
                engine.Plus_Frame.설명글.text.text = "새로 작성해주세요."
            elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.새로만들기에러ment:
                engine.Plus_Frame.날자글.text.text = ""
                engine.Plus_Frame.금액글.text.text = ""
                engine.Plus_Frame.태그글.text.text = ""
                engine.Plus_Frame.내용글.text.text = ""
                engine.Warning_Frame.창바.text.text = ""
                engine.Plus_Frame.설명글.text.text = "새로 작성해주세요"
            elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.삭제ment:
                engine.Warning_Frame.창바.text.text = ""
                engine.data.delete()
                engine.data.reMakeViewData()
                engine.data.MakeList()
                _ViewPage()
                engine.root.update()
                engine.root.after ( 650 )
                engine.root.update()
                engine.Warning_Frame.창바.text.text = engine.controlbox.추가.삭제완료ment
                engine.Warning_Frame.Active ( True , engine )
            elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장_다시쓰기ment or engine.Warning_Frame.창바.text.text == engine.controlbox.추가.저장ment:
                Event_re( id = "PlusData" )
            elif engine.Warning_Frame.창바.text.text == engine.controlbox.추가.취소ment:
                engine.Plus_Frame.날자글.text.text = ""
                engine.Plus_Frame.금액글.text.text = ""
                engine.Plus_Frame.태그글.text.text = ""
                engine.Plus_Frame.내용글.text.text = ""
                engine.Warning_Frame.창바.text.text = ""
                