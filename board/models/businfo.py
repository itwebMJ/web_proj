import requests
from bs4 import BeautifulSoup


class BusVo:
    def __init__(self, busRouteId=None,busRouteNm=None,stStationNm=None,edStationNm=None,term=None,firstBusTm=None,lastBusTm=None,corpNm=None):
        self.busRouteId = busRouteId
        self.busRouteNm = busRouteNm
        self.stStationNm = stStationNm
        self.edStationNm = edStationNm
        self.term = term
        self.firstBusTm = firstBusTm
        self.lastBusTm = lastBusTm
        self.corpNm = corpNm

    def __str__(self):
        return 'busRouteId : '+ str(self.busRouteId)+'\nbusRouteNm : '+str(self.busRouteNm)+'\nstStationNm : '\
               +self.stStationNm+'\nedStationNm : '+self.edStationNm+'\nterm :'+str(self.term)+'\nfirstBusTm :'\
               +str(self.firstBusTm)+'\nlastBusTm : '+str(self.lastBusTm)+'\ncorpNm : '+self.corpNm

class PointVo:
    def __init__(self, no=None, gpsX=None, gpsY=None):
        self.no = no
        self.gpsX = gpsX
        self.gpsY = gpsY

    def __str__(self):
        return 'no : '+str(self.no)+' ('+str(self.gpsX)+', '+str(self.gpsY)+')'

class StationVo:
    def __init__(self, seq=None, stationNm=None, arsId=None):
        self.seq = seq
        self.stationNm = stationNm
        self.arsId = arsId

    def __str__(self):
        return 'seq : '+str(self.seq)+'\nstationNm : '+self.stationNm+'\narsId : '+str(self.arsId)



class BusService:
    def __init__(self):
        self.url = 'http://ws.bus.go.kr/api/rest/busRouteInfo/%s?ServiceKey=%s&%s=%s'
        self.apiKey = '4tdDtEO6U6Iu3LUIgh5CaYYiZfUj9XrwBjOpicIiJxWHmGWOQbO8Pr9q8R8kNeptActfQZHmfho%2BT2Euxcn2zQ%3D%3D'

    def getRouteInfoItem(self, busRouteId):
        url = self.url%('getRouteInfo', self.apiKey, 'busRouteId', busRouteId)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # 파서의 종류를 xml로 지정
        code = root.find('headerCd').get_text()
        msg = root.find('headerMsg').get_text()
        print('처리결과:', msg)
        if code == '0':
            busRouteId = root.find('busRouteId').get_text()
            busRouteNm = root.find('busRouteNm').get_text()
            stStationNm = root.find('stStationNm').get_text()
            edStationNm = root.find('edStationNm').get_text()
            term = root.find('term').get_text()
            firstBusTm = root.find('firstBusTm').get_text()
            lastBusTm = root.find('lastBusTm').get_text()
            corpNm = root.find('corpNm').get_text()

            return BusVo(busRouteId, busRouteNm, stStationNm, edStationNm, term, firstBusTm, lastBusTm, corpNm)

    def getRoutePathList(self, busRouteId):
        url = self.url % ('getRoutePath', self.apiKey, 'busRouteId', busRouteId)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # 파서의 종류를 xml로 지정
        print(root)
        code = root.find('headerCd').get_text()
        msg = root.find('headerMsg').get_text()
        print('처리결과:', msg)

        vo_list = []
        if code == '0':
            itemList = root.select('itemList')
            for item in itemList:
                no = item.find('no').get_text()
                gps_x = item.find('gpsX').get_text()
                gps_y = item.find('gpsY').get_text()
                vo_list.append(PointVo(no, gps_x, gps_y))
            return vo_list

    def getBusRouteList(self, strSrch):
        url = self.url % ('getBusRouteList', self.apiKey, 'strSrch', strSrch)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # 파서의 종류를 xml로 지정
        code = root.find('headerCd').get_text()
        msg = root.find('headerMsg').get_text()
        print('처리결과:', msg)
        vo_list = []
        if code == '0':
            itemList = root.select('itemList')
            for item in itemList:

                busRouteId = item.find('busRouteId').get_text()
                busRouteNm = item.find('busRouteNm').get_text()
                stStationNm = item.find('stStationNm').get_text()
                edStationNm = item.find('edStationNm').get_text()
                term = item.find('term').get_text()
                firstBusTm = item.find('firstBusTm').get_text()
                lastBusTm = item.find('lastBusTm').get_text()
                corpNm = item.find('corpNm').get_text()
                vo_list.append(BusVo(busRouteId, busRouteNm, stStationNm, edStationNm, term, firstBusTm, lastBusTm, corpNm))
            return vo_list


    def getStaionsByRouteList(self, busRouteId):
        url = self.url % ('getStaionByRoute', self.apiKey, 'busRouteId', busRouteId)
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')  # 파서의 종류를 xml로 지정
        code = root.find('headerCd').get_text()
        msg = root.find('headerMsg').get_text()
        print('처리결과:', msg)
        vo_list = []
        if code == '0':
            itemList = root.select('itemList')
            for item in itemList:
                seq = item.find('seq').get_text()
                stationNm = item.find('stationNm').get_text()
                arsId = item.find('arsId').get_text()
                vo_list.append(StationVo(seq, stationNm, arsId))
            return vo_list
#getRouteInfoItem(노선ID): 리턴값은 BUS_VO 객체 한개 반환
# getRoutePathList(노선ID): 경로 묶음. POINT_VO객체들을 리스트에 담아서 반환
# getBusRouteList(버스명): 찾아진 버스정보를 BUS_VO 객체로 만들어서 리스트에 담아서 반환
# getStaionsByRouteList(노선ID): 찾아진 이 노선의 정거역을 STATION_VO 객체로 만들어 리스트에 담아서 반환