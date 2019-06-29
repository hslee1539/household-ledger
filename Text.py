import tkinter
import Color
class Text(object):
    """택스트를 관리합니다"""
    def __init__ ( self, text = str, sticky = tkinter.W, fontsize = "15 bold" , font = "HY견고딕",color = Color.Color.c6 ):
        self.text = text
        self.anchor = sticky
        self.font = font + " " +fontsize
        self.c = color
        self.cOrigen = color
    def FontSize ( self , num = 0 ):
        """글시 크기를 조절합니다 폰트 사이즈는 반듯이 10~99사이만 하세요 리턴값으로 이 폰트의 크기를 알 수 있습니다"""
        font = self.font + " "# 새로운 택스트를 만들기 위해서 + 함
        if num > 9:
            self.font = self.font.replace ( self.font[self.font.index(" ") + 1 : self.font.index(" ") + 3] , str(num) )
        return self.font[self.font.index(" ") + 1 : self.font.index(" ") + 3]

