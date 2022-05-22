import pandas as pd
import os
from parse import Parser
from loader import Loader
from bs4 import BeautifulSoup
from art import tprint


"""точка входа в программу"""
def main():
    tprint("Parser")

    p = Loader.loadPages()
    cards = Loader.loadCards(p)
    os.chdir("pages_html")
    pages = os.listdir()
    os.chdir("..") 

    """Столбцы с данными"""
    accommodation = []
    floor = []
    num_rooms = []
    district = []
    metro = []
    height = []

    """Названия колонок"""
    for page in pages:
        os.chdir("pages_html")
        with open(page, "r", encoding='utf-8') as f:
            text = f.read()
        soup = BeautifulSoup(text, features="lxml")
        accommodation.append(Parser.findAccomodationType(soup)) 
        floor.append(Parser.floorNumber(soup))
        num_rooms.append(Parser.numberOfRooms(soup))
        district.append(Parser.findDistrict(soup))
        metro.append(Parser.handyMetro(soup))
        print(f"len(district) {len(district[0])}", f"len(metro) {len(metro)}", f"len(num_rooms) {len(num_rooms)}", f"len(floor) {len(floor)}", f"len(accommodation): {len(accommodation)}", end="\n")
        os.chdir("..")
        os.chdir("./cards/data1")
        cards = os.listdir()
        for card in cards:
            with open(card, "r", encoding='utf-8') as f:
                text = f.read()
            soup = BeautifulSoup(text, features="lxml")
            height.append(Parser.height(soup)[0])
        print(f"len(height) {len(height)}")
        os.chdir("../..")
    print(os.getcwd())
    # os.chdir("pages_html")
    # print(len(accommodation[0]), len(floor[0]), len(district[0]), len(metro[0]),  len(num_rooms[0]),  sep=" they are not the same?\n ")
    # print(height)
    dct = {
        "Административный округ": district[0],
        "Число комнат": num_rooms[0],
        "Тип жилья": accommodation[0],
        # "Планировка комнат": plan,
        # "Санузел": wc,
        # "Балкон/Лоджия": balcony,
        "Этаж(номер)": floor[0],
        "Высота потолков": height[0],
        # "Тип дома": type,
        # "Отделка": trim,
        # "Год постройки": year,
        # "Время до ближайшего метро": metro_time[0],
        "Ближайшее метро": metro[0],
        # "Колличество указанных станций": num_stations
    }

    dataframe = pd.DataFrame(data=dct)
    dataframe.to_csv("res.csv", sep=';', index=False, encoding='utf-8')


if __name__ == '__main__':
    main()





