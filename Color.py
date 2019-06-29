class Color(object):
    """색들의 모음입니다"""
    class color1 ( str ):##설명을 추가하기 위해 따로 만듬
        """약한회색"""
    class color2 ( str ):##설명을 추가하기 위해 따로 만듬
        """강한회색"""
    class color3 ( str ):##설명을 추가하기 위해 따로 만듬
        """주황"""
    class color4 ( str ):##설명을 추가하기 위해 따로 만듬
        """하늘색(선택)"""
    class color5 ( str ):##설명을 추가하기 위해 따로 만듬
        """초록색"""
    class color6 ( str ):##설명을 추가하기 위해 따로 만듬
        """폰트색 """
    class color7 ( str ):
        """ 검정색"""
    class color8 ( str ):
        """ 회색"""
    c1 = color1("#9e9e9e")
    c2 = color2("#2f2f2f")#("#5e5e5e")
    c3 = color3("#f69210")
    c4 = color4("#418ab3")
    c5 = color5("#a6b727")
    c6 = color6("#FFFFFF")
    c7 = color7("#111111")
    c8 = color8("#333333")
class ColorChanger ( ):
    """ 어떤 오브젝트던 .c 인자를 가지면 tkinterRGB에 의해 색을 변화합니다"""
    def __init__ ( self, engine,root ,preC , afterC , object , Frame):
        """ """
        self.engine = engine
        self.root = root
        self.root.after ( 0, self.Start , preC , afterC, object, Frame , 0)
        engine.ThreadStart( )

    def Start ( self, preC , afterC, object , Frame , nowFrame ):
        """ 시작합니다 """
        nowFrame = nowFrame + 1
        R = int(preC[1:3],16)
        G = int(preC[3:5],16)
        B = int(preC[5:7],16)
        R_ = int(afterC[1:3],16)
        G_ = int(afterC[3:5],16)
        B_ = int(afterC[5:7],16)
        nextR = hex(int(R - (R - R_) * nowFrame/Frame))[2:4]
        nextG = hex(int(G - (G - G_) * nowFrame/Frame))[2:4]
        nextB = hex(int(B - (B - B_) * nowFrame/Frame))[2:4]
        object.c = "#" + nextR + nextG + nextB

        if nowFrame < Frame:
            self.root.after ( 40, self.Start , preC , afterC, object, Frame , nowFrame )
        else:
            self.engine.ThreadEnd()