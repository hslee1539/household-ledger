import Engine
import id

class event ():
    """ 키보드 이벤트를 처리합니다 """
    def __init__ ( self , engine = Engine ):
        """키보드 이벤트는 engine을 받아야 합니다. 그래야 모든 것을 제어 가능합니다."""
        self.engine = engine
        self.engine.root.bind ("<Key>", self._Event )
    def _Event ( self , e ):
        """ 이벤트를 처리합니다 """
        if e.char != "": ## 특수 기호나, 한글이 걸러짐
            if e.keycode > 47 and e.keycode < 58:##숫자들만 걸러짐
                id.Event_re ( id = "KeyEvent", char = e.char)
            elif e.keycode > 64 and e.keycode <91:##알파벳들
                id.Event_re ( id = "KeyEvent", char = e.char)
            elif '힣' > e.char and e.char > 'ㄱ':
                id.Event_re ( id = "KeyEvent", char = e.char)
            elif e.keycode == 8:
                id.Event_re ( id = "KeyEvent", char = "Eraser")
            elif e.keycode == 13:
                id.Event_re ( id = "KeyEvent", char = "Enter")
            elif e.keycode == 9:
                id.Event_re ( id = "KeyEvent", char = "Tab")
            elif e.keycode == 32:
                id.Event_re ( id = "KeyEvent", char = "Space")
        else: ## 그외 한글이나 특수 버
            if e.keycode == 0: ##한글이나, 특수문자들ㄹ 걸러짐
                id.Event_re ( id = "KeyEvent", char = e.char)
            elif e.keycode == 8:
                print("지우길를 눌렀습니다.")
                id.Event_re ( id = "KeyEvent", char = "Eraser")
    class Tool ():
        """ 키 이벤트 관련 툴들입니다. """
        def Filter ( char , mode ):
            """여기에 char값을 넣주면 mode값에 따라 숫자 또는, 한글영어로만 리턴됩니다.
            mode는 0,1의 값을 넣주고 0은 숫자만, 1은 모든글자 입니다."""
            if mode == 0:
                if char > "/" and char < ":": ### 아스키 코드 참고
                    return char
            elif mode == 1:
                if char > "@" and char < "[": ## 영어 대문자
                    return char
                elif char > "'" and char < "{": ## 영어
                    return char
                elif char > "ㄱ" and char < "힣": # 한글
                    return char
                elif char > "/" and char < ":": ### 아스키 코드 참고
                    return char
            
            if len(char) > 1:
                return char
            return ""
