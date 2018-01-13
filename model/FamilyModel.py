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
    def __init__(self, addr=None, posTel=None, post=None, pkey=None, name=None, oldpkey=None, serid=None,
                 tel=None, px=None, py=None, all=None, road=None, twoice=None,
                 isRest=None, isParking=None, isSharePot=None, isToilet=None,
                 isPhoto=None, isWiFi=None, isSunmai=None, isVeg=None, isTanhou=None, isFreshfruit=None, isTwoice=None,
                 isIcecream=None, isMuffin=None, isKantoni=None, isSweetpotato=None, isCoffee=None, isSingleOrigin=None,
                 isCOFFEEDeliver=None, isSmoothie=None, isOneice=None, town=None, updateTime=datetime.today()):
        """

        :param addr: 地址
        :param posTel: 接收傳真服務(付費)
        :param pkey: 門市店號
        :param name: 門市店名
        :param oldpkey: 
        :param serid: 
        :param tel: 電話
        :param x: 經度 Longitude
        :param y: 緯度 Latitude
        :param isSharePot: 咖啡分享 壺
        :param isCOFFEEDeliver: 咖啡外送
        :param isSingleOrigin: 單品咖啡
        :param isCoffee: Let’s Café
        :param isSweetpotato: 夯番薯
        :param isKantoni: 關東煮
        :param isMuffin: 列日鬆餅
        :param isIcecream: Fami 霜淇淋 單口味
        :param isTwoice: Fami 霜淇淋 雙口味
        :param isFreshfruit: 鮮水果
        :param isTanhou: 天和鮮物
        :param isVeg: 生鮮蔬菜
        :param isSunmai: SUNMAI 金色三麥
        :param isWiFi: Fami-WiFi
        :param isPhoto: 相片立可得
        :param isRest: 休憩區
        :param isToilet: 廁所
        :param isParking: 停車場
        :param isSmoothie:
        :param isOneice:
        :param town: town 
        :param updateTime: updateTime
        """
        self.addr = addr
        self.posTel = posTel
        self.post = post
        self.pkey = pkey
        self.name = name
        self.oldpkey = oldpkey
        self.serid = serid
        self.tel = tel
        self.px = px
        self.py = py
        self.all = all
        self.road = road
        self.twoice = twoice

        self.isSharePot = isSharePot
        self.isCOFFEEDeliver = isCOFFEEDeliver
        self.isSingleOrigin = isSingleOrigin
        self.isCoffee = isCoffee
        self.isSweetpotato = isSweetpotato
        self.isKantoni = isKantoni
        self.isMuffin = isMuffin
        self.isIcecream = isIcecream
        self.isTwoice = isTwoice
        self.isOneice = isOneice
        self.isFreshfruit = isFreshfruit
        self.isTanhou = isTanhou
        self.isVeg = isVeg
        self.isSunmai = isSunmai
        self.isWiFi = isWiFi
        self.isPhoto = isPhoto
        self.isRest = isRest
        self.isToilet = isToilet
        self.isParking = isParking
        self.isSmoothie = isSmoothie

        self.town = town
        self.updateTime = updateTime
