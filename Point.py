class Point(object):
    """좌표입니다."""
    def __init__ ( self, x=0, y=0 ):
        """Point의 생성자입니다."""
        self.x = x
        self.y = y
    def copy ( self ):
        """ 포인터를 카피합니다 리턴값이 있습니다"""
        return Point ( self.x , self.y )
    def set ( self, x ,y):
        self.x = x
        self.y = y
    def __add__ ( point1 , point2 ):
        """ 포인터들을 더합니다 (연산자 오버로딩)"""
        return Point(point1.x + point2.x , point1.y + point2.y)
    def __mul__  ( point1 , num ):
        """ 포인트의 num많큼 곱샘연산을 합니다."""
        return Point ( point1.x * num , point1.y * num )

