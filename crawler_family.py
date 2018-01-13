import requests
from xml.etree.ElementTree import fromstring, tostring
from xmljson import badgerfish as bf
import pickle
from model.FamilyModel import City, Town, Store
from urllib.parse import urlencode
import json

__URL_family__ = 'http://api.map.com.tw/net/familyShop.aspx'
__EXPORT_FILE__ = "data/city_family.dat"
__HEADER__ = {'Host': 'api.map.com.tw',
              'Connection': 'keep-alive',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
              'Accept': '*/*',
              'Referer': 'http://www.family.com.tw/marketing/inquiry.aspx',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'en-US,en;q=0.9',
              'Cookie': 'ASPSESSIONIDSCRQSSBC=NGJBKMJDKKKBEPLPINDCBMHD; ASP.NET_SessionId=zmeb31xw2uniyglbvrvuitys; ASPSESSIONIDQCRSSTBC=ECIBEGKDHALCCALIDKNBKEIP; ServerName=www%2Efamily%2Ecom%2Etw; ASPSESSIONIDQARSSSAD=PAHHJPODEBOCPEDACBNCAIAF'}
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

__STORE_PROPERTIES__ = ['oneice', 'twoice', 'Kantoni', 'SWEETPOTATO', 'COFFEE', 'veg', 'SUNMAI', 'TANHOU',
                        'Photo', 'muffin', 'Rest', 'SharePot', 'SingleOrigin', 'Smoothie', 'COFFEEDeliver',
                        'icecream', 'Toilet', 'WiFi', 'FreshFruit', 'Parking']


# Help functions
def __retrieveStore(cityName, townName):
    queryDict = {'searchType': 'ShopList',
                 'type': '',
                 'city': cityName,
                 'area': townName,
                 'road': '',
                 'fun': 'showStoreList',
                 'key': '6F30E8BF706D653965BDE302661D1241F8BE9EBC'}

    url = __URL_family__ + '?' + urlencode(queryDict)
    r = requests.post(url, headers=__HEADER__)

    stores = __extractStores(r.text)
    return stores


def __retrieveTowns(cityName):
    queryDict = {'searchType': 'ShowTownList',
                 'type': '',
                 'city': cityName,
                 'fun': 'storeTownList',
                 'key': '6F30E8BF706D653965BDE302661D1241F8BE9EBC'}

    url = __URL_family__ + '?' + urlencode(queryDict)
    r = requests.post(url, headers=__HEADER__)

    towns = __extractTowns(r.text)
    return towns


def __extractStores(rawXmlcontent):
    def __get(aDict, key, default=None):
        value = aDict.get(key, default)
        if value:
            return str(value)
        return value
    
    d = rawXmlcontent
    d = d.replace("showStoreList(", "")
    d = d.replace(")", "")
    storesRaw = json.loads(d)

    # Map to Store
    allProperty = set()
    stores = []
    for storeRaw in storesRaw:
        store = Store()
        store.name = __get(storeRaw, 'NAME')
        store.posTel = __get(storeRaw, 'POSTel')
        store.serid = __get(storeRaw, 'SERID')
        store.tel = __get(storeRaw, 'TEL')
        store.addr = __get(storeRaw, 'addr')
        store.all = __get(storeRaw, 'all')
        store.oldpkey = __get(storeRaw, 'oldpkey')
        store.pkey = __get(storeRaw, 'pkey')
        store.post = __get(storeRaw, 'post')
        store.px = __get(storeRaw, 'px')
        store.py = __get(storeRaw, 'py')
        store.road = __get(storeRaw, 'road')
        store.twoice = __get(storeRaw, 'twoice')

        print(store.name + ', ' + store.addr)

        if store.all:
            if 'COFFEE' in store.all:
                store.isCoffee = 'Y'
            if 'SharePot' in store.all:
                store.isSharePot = 'Y'
            if 'SWEETPOTATO' in store.all:
                store.isSweetPotato = 'Y'
            if 'WiFi' in store.all:
                store.isWiFi = 'Y'
            if 'twoice' in store.all:
                store.isTwoice = 'Y'
            if 'oneice' in store.all:
                store.isOneice = 'Y'
            if 'SingleOrigin' in store.all:
                store.isSingleOrigin = 'Y'
            if 'muffin' in store.all:
                store.isMuffin = 'Y'
            if 'COFFEEDeliver' in store.all:
                store.isCoffeeDeliver = 'Y'
            if 'Toilet' in store.all:
                store.isToilet = 'Y'
            if 'SUNMAI' in store.all:
                store.isSunmai = 'Y'
            if 'Photo' in store.all:
                store.isPhoto = 'Y'
            if 'veg' in store.all:
                store.isVeg = 'Y'
            if 'Rest' in store.all:
                store.isRest = 'Y'
            if 'icecream' in store.all:
                store.isIcecream = 'Y'
            if 'Smoothie' in store.all:
                store.isSmoothie = 'Y'
            if 'Kantoni' in store.all:
                store.isKantoni = 'Y'
            if 'TANHOU' in store.all:
                store.isTanhou = 'Y'
            if 'FreshFruit' in store.all:
                store.isFreshfruit = 'Y'
            if 'Parking' in store.all:
                store.isParking = 'Y'

            for feature in store.all.split(','):
                allProperty.add(feature)
        stores.append(store)

    # Property
    for p in allProperty:
        if p not in __STORE_PROPERTIES__:
            print(p + ' uncatch property')
            exit(1)
    return stores


def __extractTowns(rawXmlcontent):
    d = rawXmlcontent
    d = d.replace("storeTownList(", "")
    d = d.replace(")", "")
    townsRaw = json.loads(d)

    towns = [Town(str(townRaw['post']), str(townRaw['town'])) for townRaw in townsRaw]
    return towns


def __parseCities(cityData):
    cities = [City(data[0], data[1]) for data in cityData]
    return cities


def __main__():
    # Load data
    cities = __parseCities(__CITY_DATA__)

    # Get town
    for city in cities:
        towns = __retrieveTowns(city.name)
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
