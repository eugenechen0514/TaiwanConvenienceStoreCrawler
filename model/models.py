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

        :param address: 
        :param faxNo: 
        :param poiid: 猜測是門市id
        :param poiName: 猜測是門市名字
        :param specialStoreKind: 
        :param storeUrl: 
        :param telno: 
        :param x: 
        :param y: 
        :param is7WiFi: 
        :param isATM: 
        :param isCityCafe: 
        :param isCorn: 
        :param isDining: 
        :param isFruit: 
        :param isHealthStations: 
        :param isHotDog: 
        :param isIbon: 
        :param isIce: 
        :param isIceCream: 
        :param isKindRoom: 
        :param isLavatory: 
        :param isMakeup: 
        :param isMisterDonuts: 
        :param isMuji: 
        :param isOpenStore: 
        :param isOrganic: 
        :param isParking: 
        :param isStarBucks: 
        :param isSweetPotato: 
        :param isTea: 
        :param isUnionPay: 
        :param isVitalityHealth: 
        :param town: town 
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
