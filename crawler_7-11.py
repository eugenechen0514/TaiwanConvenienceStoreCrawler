import requests
from xml.etree.ElementTree import fromstring, tostring
from xmljson import badgerfish as bf
import pickle
from model.models import City, Town, Store


__URL_7_11__ = 'http://emap.pcsc.com.tw/EMapSDK.aspx'
__EXPORT_FILE__ = "data/city_7_11.dat"
__CITY_DATA__ = [('01', '台北市'),
                 ('02', '基隆市'),
                 ('03', '新北市'),
                 ('04', '桃園市'),
                 ('05', '新竹市'),
                 ('06', '新竹縣'),
                 ('07', '苗栗縣'),
                 ('08', '台中市'),
                 # ('09', '0000'),
                 ('10', '彰化縣'),
                 ('11', '南投縣'),
                 ('12', '雲林縣'),
                 ('13', '嘉義市'),
                 ('14', '嘉義縣'),
                 ('15', '台南市'),
                 # ('16', '0000'),
                 ('17', '高雄市'),
                 # ('18', '0000'),
                 ('19', '屏東縣'),
                 ('20', '宜蘭縣'),
                 ('21', '花蓮縣'),
                 ('22', '台東縣'),
                 ('23', '澎湖縣'),
                 ('24', '連江縣'),
                 ('25', '金門縣')
                 ]


# Help functions
def __retrieveStore(cityName, townName):
    payload = {'commandid': 'SearchStore', 
               'city': cityName, 
               'town': townName,
               'isDining': 'False',
               'isParking': 'False',
               'isLavatory': 'False', 
               'isATM': 'False', 
               'is7WiFi': 'False', 
               'isIce': 'False', 
               'isHotDog': 'False', 
               'isHealthStations': 'False', 
               'isIceCream': 'False',
               'isOpenStore': 'False', 
               'isFruit': 'False',
               'isCityCafe': 'False', 
               'isUp': 'False', 
               'isOrganic': 'False', 
               'isCorn': 'False', 
               'isMakeUp': 'False', 
               'isMuji': 'False', 
               'isMD': 'False', 
               'isStarBucks': 'False', 
               'isIbon': 'False',
               'isTea': 'False', 
               'isSweetPotato': 'False', 
               'isVitalityHealth': 'False', 
               'isKidRoom': 'False'}
    r = requests.post(__URL_7_11__, payload)
    stores = __extractStores(r.text)
    return stores


def __retrieveTowns(cityid):
    payload = {'commandid': 'GetTown',
               'cityid': cityid,
               'isDining': 'False',
               'isParking': 'False',
               'isLavatory': 'False',
               'isATM': 'False',
               'is7WiFi': 'False',
               'isIce': 'False',
               'isHotDog': 'False',
               'isHealthStations': 'False',
               'isIceCream': 'False',
               'isOpenStore': 'False',
               'isFruit': 'False',
               'isCityCafe': 'False',
               'isUp': 'False',
               'isOrganic': 'False',
               'isCorn': 'False',
               'isMakeUp': 'False',
               'isMuji': 'False',
               'isMD': 'False',
               'isStarBucks': 'False',
               'isIbon': 'False',
               'isTea': 'False',
               'isSweetPotato': 'False',
               'isVitalityHealth': 'False',
               'isKidRoom': 'False'}

    r = requests.post(__URL_7_11__, payload)

    towns = __extractTowns(r.text)
    return towns


def __extractStores(rawXmlcontent):
    def __get(aDict, key, default=None):
        value = aDict.get(key, default)

        # Check empty dict
        if not bool(value):
            value = default
        else:
            value = value.get('$', default)
        return value

    d = rawXmlcontent
    a = fromstring(d)
    c = bf.data(a)
    geoPositionElement = c['iMapSDKOutput'].get('GeoPosition', None)

    # No stores
    if geoPositionElement is None:
        return []

    # Only one store
    positions = []
    if isinstance(geoPositionElement, list):
        positions = geoPositionElement
    else:
        positions = [geoPositionElement]

    # Map to Store
    stores = []
    for position in positions:
        store = Store()
        store.address = str(__get(position, 'Address'))
        store.faxNo = str(__get(position, 'FaxNo'))
        store.poiid = str(__get(position, 'POIID'))
        store.poiName = str(__get(position, 'POIName'))
        store.specialStoreKind = str(__get(position, 'SpecialStore_Kind'))
        store.storeUrl = str(__get(position, 'Store_URL'))
        store.telno = str(__get(position, 'Telno'))
        store.x = str(__get(position, 'X'))
        store.y = str(__get(position, 'Y'))
        store.is7WiFi = str(__get(position, 'is7WiFi'))
        store.isATM = str(__get(position, 'isATM'))
        store.isCityCafe = str(__get(position, 'isCityCafe'))
        store.isCorn = str(__get(position, 'isCorn'))
        store.isDining = str(__get(position, 'isDining'))
        store.isFruit = str(__get(position, 'isFruit'))
        store.isHealthStations = str(__get(position, 'isHealthStations'))
        store.isHotDog = str(__get(position, 'isHotDog'))
        store.isIbon = str(__get(position, 'isIbon'))
        store.isIce = str(__get(position, 'isIce'))
        store.isIceCream = str(__get(position, 'isIceCream'))
        store.isKidRoom = str(__get(position, 'isKidRoom'))
        store.isLavatory = str(__get(position, 'isLavatory'))
        store.isMakeup = str(__get(position, 'isMakeup'))
        store.isMisterDonuts = str(__get(position, 'isMisterDonuts'))
        store.isMuji = str(__get(position, 'isMuji'))
        store.isOpenStore = str(__get(position, 'isOpenStore'))
        store.isOrganic = str(__get(position, 'isOrganic'))
        store.isParking = str(__get(position, 'isParking'))
        store.isStarBucks = str(__get(position, 'isStarBucks'))
        store.isSweetPotato = str(__get(position, 'isSweetPotato'))
        store.isTea = str(__get(position, 'isTea'))
        store.isUnionPay = str(__get(position, 'isUnionPay'))
        store.isVitalityHealth = str(__get(position, 'isVitalityHealth'))
        stores.append(store)
    return stores


def __extractTowns(rawXmlcontent):
    d = rawXmlcontent
    # d = d.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    a = fromstring(d)
    c = bf.data(a)
    geoPositionList = c['iMapSDKOutput']['GeoPosition']
    towns = [Town(str(position['TownID']['$']), position['TownName']['$'], str(position['X']['$']), str(position['Y']['$'])) for position in geoPositionList]
    return towns


def __parseCities(cityData):
    cities = [City(data[0], data[1]) for data in cityData]
    return cities


def __main__():
    # data loader
    cities = __parseCities(__CITY_DATA__)

    # Get town
    for city in cities:
        towns = __retrieveTowns(city.id)
        city.towns = towns

    # Get store
    for city in cities:
        allCityStores = []
        for town in city.towns:
            print("Start: (" + city.name + ", " + town.name + ")")
            stores = __retrieveStore(city.name, town.name)
            town.stores = stores
            allCityStores += stores

            # other connection
            for store in stores:
                store.town = town
        city.stores = allCityStores

    # Export
    pickle.dump(cities, open(__EXPORT_FILE__, "wb"))

__main__()
