# Class def
from datetime import datetime


class City:
    def __init__(self, id="", name="", towns=[], stores=[]):
        self.name = name
        self.id = id
        self.towns = towns
        self.stores = stores


class Town:
    def __init__(self, id="", name="", x="", y="", stores=[]):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.stores = stores


class Store:
    def __init__(self, address=None, faxNo=None, poiid=None, poiName=None, specialStoreKind=None, storeUrl=None,
                 telno=None, x=None, y=None, is7WiFi=None, isATM=None, isCityCafe=None, isCorn=None, isDining=None,
                 isFruit=None, isHealthStations=None, isHotDog=None, isIbon=None, isIce=None, isIceCream=None,
                 isKindRoom=None, isLavatory=None, isMakeup=None, isMisterDonuts=None, isMuji=None, isOpenStore=None,
                 isOrganic=None, isParking=None, isStarBucks=None, isSweetPotato=None, isTea=None, isUnionPay=None,
                 isVitalityHealth=None, town=None, updateTime=datetime.today()):
        """

        :param address: 地址
        :param faxNo: 接收傳真服務(付費)
        :param poiid: 門市店號
        :param poiName: 門市店名
        :param specialStoreKind: 
        :param storeUrl: 
        :param telno: 電話
        :param x: 經度 Longitude
        :param y: 緯度 Latitude
        :param is7WiFi: ibon WiFi
        :param isATM: ATM
        :param isCityCafe: 外送咖啡服務
        :param isCorn: 黃金玉米(蒸煮)
        :param isDining: 座位區
        :param isFruit: 
        :param isHealthStations: 千禧健康小站
        :param isHotDog: 
        :param isIbon: ibon
        :param isIce: 思樂冰
        :param isIceCream: 霜淇淋
        :param isKindRoom: 
        :param isLavatory: 廁所
        :param isMakeup: 美妝
        :param isMisterDonuts: Mister Donuts 甜甜圈
        :param isMuji: 無印良品
        :param isOpenStore: OPEN! STORE
        :param isOrganic: 台塑有機蔬菜
        :param isParking: 停車場
        :param isStarBucks: 
        :param isSweetPotato: 
        :param isTea: 現萃茶
        :param isUnionPay: 
        :param isVitalityHealth: 生機活力健康專區
        :param town: town 
        :param updateTime: updateTime
        """
        self.address = address
        self.faxNo = faxNo
        self.poiid = poiid
        self.poiName = poiName
        self.specialStoreKind = specialStoreKind
        self.storeUrl = storeUrl
        self.telno = telno
        self.x = x
        self.y = y
        self.is7WiFi = is7WiFi
        self.isATM = isATM
        self.isCityCafe = isCityCafe
        self.isCorn = isCorn
        self.isDining = isDining
        self.isFruit = isFruit
        self.isHealthStations = isHealthStations
        self.isHotDog = isHotDog
        self.isIbon = isIbon
        self.isIce = isIce
        self.isIceCream = isIceCream
        self.isKidRoom = isKindRoom
        self.isLavatory = isLavatory
        self.isMakeup = isMakeup
        self.isMisterDonuts = isMisterDonuts
        self.isMuji = isMuji
        self.isOpenStore = isOpenStore
        self.isOrganic = isOrganic
        self.isParking = isParking
        self.isStarBucks = isStarBucks
        self.isSweetPotato = isSweetPotato
        self.isTea = isTea
        self.isUnionPay = isUnionPay
        self.isVitalityHealth = isVitalityHealth

        self.town = town
        self.updateTime = updateTime
