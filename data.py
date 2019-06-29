import FILE

class Data ( ):
    """ 가계부의 데이타를 관리합니다 """
    class tool ():
        """ 편의기능을 제공하는 툴들입니다.상위 클래스인 Data와 다른점은 self예약어가 없습니다 """
        def copyData ( datas ):
            """ 레퍼런스에 구애 받지 않고 카피 하고 싶으면 사용하세요"""
            returnData = []
            i = 0
            while i < len ( datas ):
                returnData.append ( datas[i] )
                i = i + 1
            return returnData
        def plusData ( datas, 수익 = True):
            """데이타의 금액중 수익또는 지출만 더합니다 """
            returnData = 0
            i = 0
            print("Data.tool.plusData.", datas)
            while i < len ( datas ):
                if datas[i]["금액"] > 0 and 수익==True:
                    returnData = returnData + datas[i]["금액"]
                elif datas[i]["금액"] < 0 and 수익==False:
                    returnData = returnData + datas[i]["금액"]
                i = i + 1
            return returnData
        def percentData ( datas ):
            """ 금액을 퍼센트화 합니다 수익은 양수, 지출은 음수로 반환합니다."""
            returnData = datas.copy()
            money = Data.tool.plusData ( datas, True ) # 가지고 있는 돈
            i = 0
            while i < len ( datas ):
                returnData[i]["금액"] = int ( returnData[i]["금액"] / money * 100 )
                i = i + 1
            return returnData
        def removeEnter ( datas ):
            returnData = []
            i = 0
            while i < len ( datas ):
                returnData.append (datas[i].replace("\n","") )
                i = i + 1
            return returnData
    def __init__ ( self ):
        self.메인데이타 = []
        임시데이타 = FILE.io.read ( )
        self.메인데이타 = 임시데이타
        
    def save ( self ):
        FILE.io.save ( self.메인데이타 )
    def testData (self ):
        """ 테스트용입니다 """
        self.메인데이타 = [{'날자': 20160101, '금액': 100000, '내용': '용돈', '태그': '#용돈'}, {'날자': 20160102, '금액': -1400, '내용': '버스값', '태그': '#교통'}, {'날자': 20160102, '금액': -4500, '내용': '밥값', '태그': '#식사'}, {'날자': 20160102, '금액': -5500, '내용': '택시', '태그': '#교통'}, {'날자': 20160104, '금액': -34000, '내용': '휴대폰 할부', '태그': '#할부'}, {'날자': 20160104, '금액': -7500, '내용': '영화관람', '태그': '#여가'}]
    def createArray ( self , tag ):
        """ 메인데이타에서 날자, 금액, 내용, 태그중 하나를 입력하고 이것을 가지고 배열을 만듭니다"""
        returnData = []
        i = 0
        while len ( self.메인데이타 ) > i :
            returnData.append ( self.메인데이타[i][tag] )
            i = i + i
        return returnData
    def sortData ( self , tag ):
        """ tag이름으로 정렬합니다."""
        returnData = []
        returnData = self.메인데이타.copy()
        sortKey = []
        sortData = {}
        i = 0
        
        if tag == "날자" or tag == "금액":
            i = 0
            while i < len ( returnData ) :
                ii = 0
                while True:
                    try:
                        sortData[ returnData[i][tag] * 100 + ii]
                        ii = ii + 1
                    except:
                        sortData.update ( { returnData[i][tag] * 100 + ii : returnData[i] })
                        sortKey.append ( returnData[i][tag] * 100 + ii )
                        break
                i = i + 1
        else :
            i = 0
            while i < len ( returnData ) :
                ii = 0
                while True:
                    try:
                        sortData[ returnData[i][tag] * 100 + ii]
                        ii = ii + 1
                    except:
                        sortData.update ( { returnData[i][tag] + str(ii) : returnData[i] })
                        sortKey.append ( returnData[i][tag] + str(ii) )
                        break
                i = i + 1
        a = 0
        sortKey.sort( ) ## 정렬
        if len (sortKey) == len (returnData):
            i = 0
            while i < len ( sortKey ):
                returnData[i] = sortData[sortKey[i]]
                i = i + 1
        else:
            print("오류")
        return returnData
    def sumsameList ( self, tag ):
        """ 날자 태그중 하나 입력하고 중복된것은 금액이 합산되어 리스트 만듭니다 참고로 태그와 금액을 가지고있는 리스트가 반환됩니다"""
        returnData = []
        bufferData = {}
        bufferData2 = []
        bufferData3 = {}
        MainDataCopy = self.메인데이타.copy()
        

        if tag == "태그":
            i = 0
            while i < len ( MainDataCopy ):# 새로 추가 된것인지 검사
                try:
                    bufferData[MainDataCopy[i][ tag ]] = bufferData[MainDataCopy[i][ tag ]] + MainDataCopy[i][ "금액" ]
                except:
                    bufferData.update ( {MainDataCopy[i][ tag ] : MainDataCopy[i][ "금액" ] } )
                i = i + 1
            i = 0
            keys = list (bufferData.keys() )
            while i < len ( bufferData ):# 정렬을 위해 준비
                bufferData2.append ( bufferData[keys[i]] )
                bufferData3.update ( { bufferData[keys[i]] : keys[i] } )
                i = i + 1
            bufferData2.sort()#정렬
            i = 0
            while i < len ( bufferData2 ):# 반환 데이타를 만듬
                returnData.append ( {"태그": bufferData3[ bufferData2[i] ],"금액" :bufferData2[i] } )
                i = i + 1
        return returnData
    def _MakeTagData ( self , id ):
        """ 해당 아이디로 사전형 데이타를 만듭니다 예) { "아이디값" : [해당메인데이타값] } """
        i = 0
        returnData = {}
        while i < len ( self.메인데이타 ) :
            returnData.update ( {self.메인데이타[i][id] : self.메인데이타[i] } )
            i = i + 1
        return returnData
    def MakeViewData ( self , id ):
        """ ViewData를 갱신합니다 """
        self.page = 0
        self.id = id
        self.ViewData = self.sortData ( id )
    def reMakeViewData ( self ):
        """ viewData를 다시 만듭니다. re가 안붙은거랑은 page랑 id를 건들지 않습니다."""
        self.ViewData = self.sortData ( self.id )
        return
    def PageUp (self):
        """페이지를 업할때 호출하세요 """
        if self.page + 1 < len ( self.ViewData ):
            self.page = self.page + 1
    def PageDown ( self ):
        """페이지를 다운할때 호출하세요"""
        if self.page > 0:
            self.page = self.page - 1
    def MakeList ( self ):
        """ViewData를 최종적으로 뼈대를 만듭니다. 3개의 항을 가진 리스트를 반홥합니다"""
        returnData = []
        if self.page > 0:
            returnData.append ( self.ViewData[self.page - 1][self.id] )
        else:
            returnData.append ( "   " )
        returnData.append ( self.ViewData[self.page] )
        if self.page + 1 < len ( self.ViewData ):
            returnData .append ( self.ViewData[ self.page + 1 ][ self.id ] )
        else:
            returnData.append ( "   " )
        return returnData
    def delete ( self ):
        """조회 페이지에서 보고있는 것을 삭제합니다."""
        self.메인데이타.remove ( self.ViewData[self.page])
        return
    def PlusData ( self, **args ):
        """ PlusData(**args)는 날자 , 금액, 태그, 내용 키를 가지고 입력을 하면, 새로 데이타에 추가합니다
        리턴값으로 오류 내용을 출력합니다.
        Data.tool.plusData와 이름이 유사하니 주의하세요."""
        if len(args["날자"]) == 8:
            if (args["날자"])[0:4] > "1900" and (args["날자"])[0:4] < "2100":
                if (args["날자"])[4:6] > "00" and (args["날자"])[4:6] < "13":
                    if (args["날자"])[6:8] > "00" and (args["날자"])[6:8] < "32":
                        print("날자오류 없음")
                    else:
                        return "날자에서 일수를 확인하세요. :("
                else:
                    return "날자에서 월수를 확인하세요. :("
            else:
                return "날자에서 년수를 확인하세요. :("
        else:
            return "날자를 8글자 입력하세요. :("
        if args["금액"] =="":
            return "금액이 입력되지 않았습니다. :("
        elif -int(args["금액"]) > Data.tool.plusData( self.메인데이타 , True ) + Data.tool.plusData( self.메인데이타 , False ):
            return "금액에서 현재 가지고 있는 돈보다 많습니다. :("
        if len (args["태그"]) > 4:
            return "태그가 너무 길어요.\n 간단하고 알기 쉽게 입력하세요. :("
        if args["태그"] == "" or args["태그"] == "#":
            args["태그"] = "#기타"
        self.메인데이타.append( {"날자":int(args["날자"]) , "금액":int(args["금액"]) , "태그":args["태그"] , "내용":args["내용"] } )
        return "성공"