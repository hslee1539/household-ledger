import data

class io ():
    def read ():
        data = []
        try:
            file = open ( "Data.txt" , "r" )
        except:
            file = open ( "Data.txt" , "w" )
            file.close()
            file = open ( "Data.txt" , "r" )
        i = 0
        while True:
            data.append ( file.readline() )
            print(data[i])
            if data[i][0:1] == " ":
                data[i] = data[i][1:]
            try:
                data.index ( "" )
                data.remove( "" )
                break
            except:
                print(".")
            i = i + 1
        return io._data2MainData ( data )
    def save (datas):
        file = open ("Data.txt", "w")
        i = 0
        print("마지막 저장하기전 Data = ", datas)
        while i < len ( datas ):
            file.writelines ( str(datas[i]["날자"]) + "\n")
            file.writelines ( str(datas[i]["금액"]) + "\n")
            file.writelines ( datas[i]["태그"] + "\n ")
            if i < len ( datas ) - 1 :
                file.writelines ( datas[i]["내용"] + "\n " )
            else:
                file.writelines ( datas[i]["내용"] )
            i = i + 1
        file.close()
    def _data2MainData ( datas ):
        임시데이타 = data.Data.tool.removeEnter ( datas )
        returnData = []
        if len ( 임시데이타 ) % 4 == 0:
            i = 0
            while len ( 임시데이타 ) - 1 > i: # base 1 과 base 0 의 변환 때문에 -1
                returnData.append ( {"날자":int(임시데이타[i]) , "금액":int(임시데이타[i + 1]) , "태그":임시데이타[i + 2] , "내용":임시데이타[i + 3] } )
                i = i + 4
        return returnData
        
