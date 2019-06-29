import Object
from Point import *
from Color import *
#아 유니코드 지원 불실하네....
#
#
#

def SizeUp ( object , engine, Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeUp , object , engine , Frame, 0 , 0)
def _SizeUp ( object, engine , Frame , nowFrame , start ):
    object.pSize.y = object.pSizeORIGEN.y / Frame / Frame * nowFrame * nowFrame + start
    nowFrame = nowFrame + 1
    if  nowFrame < Frame + 1:
        engine.root.after ( 20 , _SizeUp , object , engine , Frame, nowFrame , start )
    else:
        engine.ThreadEnd()
def SizeUpChangeColor ( object , engine , Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeUp , object , engine , Frame, 0 , object.pSize.y)
    ColorChanger(engine , engine.root , Color().c3 , object.GetOrigenColor(),object , 20 )

def SizeDown ( object , engine, Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeDown , object , engine , Frame, 0, object.pSizeORIGEN.y )
def _SizeDown ( object, engine , Frame , nowFrame , start ):
    object.pSize.y = object.pSizeORIGEN.y / Frame / Frame * ( nowFrame - Frame ) * ( nowFrame - Frame ) + start - object.pSizeORIGEN.y;
    nowFrame = nowFrame + 1
    if  nowFrame < Frame + 1:
        engine.root.after ( 20 , _SizeDown , object , engine , Frame, nowFrame , start )
    else:
        engine.ThreadEnd()
def SizeUpDown ( object, engine, Frame, startp , endp ):
    engine.ThreadStart ()
    engine.root.after ( 0, _SizeUpDown , object , engine, Frame, 0 , startp , endp )
def _SizeUpDown ( object, engine, Frame, nowFrame ,startp, endp):
    object.pSize.y = ((( endp - startp )* nowFrame * nowFrame ) / (Frame * Frame) ) + startp
    nowFrame = nowFrame + 1
    if  nowFrame < Frame + 1:
        engine.root.after ( 20 , _SizeUpDown , object , engine , Frame, nowFrame , startp , endp )
    else:
        engine.ThreadEnd()



def SizeDownChangeColor ( object , engine, Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeDown , object , engine , Frame, 0, object.pSize.y )
    ColorChanger(engine , engine.root , object.GetOrigenColor(), Color().c3 ,object , 10 )

def SizeRight ( object , engine, Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeRight , object , engine , Frame, 0 , object.pSize.x)
def _SizeRight ( object, engine , Frame , nowFrame , start ):
    object.pSize.x = object.pSizeORIGEN.x / Frame / Frame * nowFrame * nowFrame + start
    nowFrame = nowFrame + 1
    if  nowFrame < Frame + 1:
        engine.root.after ( 20 , _SizeRight , object , engine , Frame, nowFrame , start )
    else:
        engine.ThreadEnd()

def SizeLeft ( object , engine, Frame ):
    engine.ThreadStart ()
    engine.root.after ( 0 , _SizeLeft , object , engine , Frame, 0, object.pSize.x )
def _SizeLeft ( object, engine , Frame , nowFrame , start ):
    nowFrame = nowFrame + 1
    object.pSize.x = object.pSizeORIGEN.x / Frame / Frame * ( nowFrame - Frame ) * ( nowFrame - Frame ) + start - object.pSizeORIGEN.x;
    if  nowFrame < Frame:
        engine.root.after ( 20 , _SizeLeft , object , engine , Frame, nowFrame , start )
    else:
        engine.ThreadEnd()

def FontSize ( Object , engine, Frame , start, end ):
    """ 폰트의 크기가 변하는 이벤트입니다"""
    engine.ThreadStart ()
    engine.root.after ( 0 , _FontSize , Object, engine ,  Frame , 0 , start , end )
def _FontSize ( Object , engine , Frame , nowFrame , starting , ending ):
    Object.text.FontSize ( int((( ending - starting )* nowFrame * nowFrame ) / (Frame * Frame) ) + starting )

    nowFrame = nowFrame + 1
    if  nowFrame < Frame + 1:
        engine.root.after ( 20 , _FontSize , Object, engine , Frame , nowFrame , starting, ending )
    else:
        engine.ThreadEnd()
def Move ( Object , engine , Frame, start , end ):
    """ 오브젝트를 이동시킵니다 """
    engine.ThreadStart()
    engine.root.after ( 0 , _Move_Origen , Object , engine , Frame , 0 , start , end )
    #engine.root.after ( 0 , _Move , Object , engine , Frame , 1 , start , end , 0, 1)
def _Move ( Object , engine , Frame , nowFrame , start , end, f , df ):
    f = f + df #시그마 속의 원소
    ff = f + 1 # 시그마 완료된 값
    df = df + 3 * int((nowFrame/Frame) > 0.2 )
    Object.pStart.x = ( end.x - start.x ) * f/ff +start.x
    Object.pStart.y = ( end.y - start.y ) * f/ff +start.y
    print(Object , "의 y  =  " , Object.pStart.y)
    nowFrame = nowFrame + 1
    if nowFrame < Frame :
        engine.root.after ( 20 , _Move , Object , engine , Frame , nowFrame , start , end , f , df )
    else:
        Object.pStart.x = end.x # 레퍼런스라 pSize = end해버리면
        Object.pStart.y = end.y # 동시에 사용할때 꼬이면 큰일 날것을 대비
        engine.ThreadEnd ()
def _Move_Origen ( Object , engine , Frame , nowFrame , start , end ):
    f = -( nowFrame - 2*Frame ) * nowFrame / (Frame * Frame)
    #f = f * f * f * f
    Object.pStart.x = ( end.x - start.x ) * f +start.x
    Object.pStart.y = ( end.y - start.y ) * f +start.y
    nowFrame = nowFrame + 1
    if nowFrame < Frame + 1 :
        engine.root.after ( 20 , _Move_Origen , Object , engine , Frame , nowFrame , start , end )
    else:
        Object.pStart.x = end.x # 레퍼런스라 pSize = end해버리면
        Object.pStart.y = end.y # 동시에 사용할때 꼬이면 큰일 날것을 대비
        engine.ThreadEnd ()


def SizeChange ( Object , engine , Frame, start , end ):
    """ 오브젝트를 이동시킵니다 start와 end에 Point값을 넣주세요."""
    engine.ThreadStart()
    engine.root.after ( 0 , _SizeChange , Object , engine , Frame , 1 , start , end , 0,1 )
def _SizeChange ( Object , engine , Frame , nowFrame , start , end , f , df):
    f = f + df #시그마 속의 원소
    ff = f + 1 # 시그마 완료된 값

    df = df + 3 * int((nowFrame/Frame) > 0.2 )
    
    Object.pSize.x = ( end.x - start.x ) * f/ff +start.x
    Object.pSize.y = ( end.y - start.y ) * f/ff +start.y
    nowFrame = nowFrame + 1
    if nowFrame < Frame :
        engine.root.after ( 20 , _SizeChange , Object , engine , Frame , nowFrame , start , end, f, df )
    else:
        Object.pSize.x = end.x # 레퍼런스라 pSize = end해버리면
        Object.pSize.y = end.y # 동시에 사용할때 꼬이면 큰일 날것을 대비
        engine.ThreadEnd ()
def SizeChange_FastToSlow ( Object , engine , Frame, start , end ):
    """ 오브젝트를 이동시킵니다 start와 end에 Point값을 넣주세요."""
    engine.ThreadStart()
    engine.root.after ( 0 , _SizeChange_FastToSlow , Object , engine , Frame , 0 , start , end )
def _SizeChange_FastToSlow ( Object , engine , Frame , nowFrame , start , end ):
    f = -( nowFrame - 2*Frame ) * nowFrame / (Frame * Frame)
    Object.pSize.x = ( end.x - start.x ) * f + start.x
    Object.pSize.y = ( end.y - start.y ) * f + start.y
    nowFrame = nowFrame + 1
    if nowFrame < Frame + 1 :
        engine.root.after ( 20 , _SizeChange_FastToSlow , Object , engine , Frame , nowFrame , start , end )
    else:
        engine.ThreadEnd ()


def MoveList ( List , engine , Frame, start , end ):
    """ List에 오브젝트들을 리스트로 묶고 대입해주세요 그러면 자동으로 여러개가 Move됩니다 (미완성 DO NOT USE)"""
    i = 0
    while i < len ( List ):
        engine.ThreadStart ()

        i = i + 1
