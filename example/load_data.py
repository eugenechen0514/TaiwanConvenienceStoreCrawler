import pickle
from model.models import City, Town, Store

__EXPORT_FILE__ = "../data/city_7_11.dat"


def __main__():
    cities = pickle.load(open(__EXPORT_FILE__, "rb"))

    print("=======================")
    for city in cities:
        print(city.name + " 有 " + str(len(city.stores)) + " 個營業處")

    print("=======================")
    for city in cities:
        for town in city.towns:
            print(city.name + town.name + " 有 " + str(len(town.stores)) + " 個營業處")

__main__()
