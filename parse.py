# import os
from bs4 import BeautifulSoup


"""класс, отвечающий за парсинг"""
class Parser:
    """поиск типа жилья"""
    def findAccomodationType(soup, accomodation = [], div = [], temp = []):
        for node in soup.findAll("span", {"data-mark": "OfferTitle"}):
            div.append(node.findAll(text=True))
        for node in soup.findAll("div", {"class": "_93444fe79c--subtitle--vHiOV"}):
            temp.append(node.findAll(text=True))
        for data in range(len(div)):
            if div[data][0][0].isdigit():
                continue
            else:
                div[data] = temp[0]
                temp.pop(0)
        for i in range(len(div)):
            if div[i][0].split(" ")[1][0].isdigit():
                accomodation.append("no type")
            else:
                accomodation.append(div[i][0].split(" ")[1])
        return accomodation


    """функция поиска этажа"""
    def floorNumber(soup, floor = [], temp = [], div = []):
        for node in soup.findAll("span", {"data-mark": "OfferTitle"}):
            div.append(node.findAll(text=True))
        for node in soup.findAll("div", {"class": "_93444fe79c--subtitle--vHiOV"}):
            temp.append(node.findAll(text=True))
        for data in range(len(div)):
            if div[data][0][0].isdigit():
                continue
            else:
                div[data] = temp[0]
                temp.pop(0)
        for i in range(len(div)):

            if div[i][0].split(" ")[4][0].isdigit():
                floor.append(div[i][0].split(" ")[4])
            else:
                floor.append("floor did not specified")
        return floor


    """функция поиска числа комнат"""
    def numberOfRooms(soup, num_rooms = [], temp = [], div = []):
        for node in soup.findAll("span", {"data-mark": "OfferTitle"}):
            div.append(node.findAll(text=True))
        for node in soup.findAll("div", {"class": "_93444fe79c--subtitle--vHiOV"}):
            temp.append(node.findAll(text=True))
        for data in range(len(div)):
            if div[data][0][0].isdigit():
                continue
            else:
                div[data] = temp[0]
                temp.pop(0)
        for data in range(len(div)):
            num_rooms.append(div[data][0][0])
        return num_rooms


    """функция поиска региона"""
    def findDistrict(soup, district = [], div = []):
        for node in soup.find_all("div", {"class": "_93444fe79c--labels--L8WyJ"}):
            div.append(node.findAll(text=True))
        for _ in range(len(div)):
            district.append(div[_][2])
        return district


    """функция поиска времени до ближайшего метро"""
    def timeToUnd(soup, metro_time = [], div = []):
        for node in soup.find_all("div", {"class": "_93444fe79c--remoteness--q8IXp"}):
            div.append(node.findAll(text=True))
        for _ in range(len(div)):
            metro_time.append(div[_][0])

        return metro_time


    """функция поиска ближайшего метро"""
    def handyMetro(soup, metro = [], temp = []):
        for node in soup.find_all("div", {"class": "_93444fe79c--labels--L8WyJ"}):
            temp.append(node.findAll(text=True))
        for _ in range(len(temp)):
            metro.append(temp[_][6])

        return metro
    
    """функция поиска высоты потолков"""
    def height(soup, temp = []):
        for node in soup.find_all("span", {"class": "a10a3f92e9--value--Y34zN"}):
            temp.append(node.findAll(text=True))
        return temp[2]


# path = './cards/data1/67295232.html'
# path = './pages_html/data5.html'
# with open(path, "r", encoding='utf-8') as f:
#     text = f.read()

# print(os.listdir())


# soup = BeautifulSoup(text, features="lxml")


# print(Parser.timeToUnd(soup))



# # print(Parser.height(soup))
# print(Parser.handyMetro(soup))


# """finding floor height"""
# def floorHeight(soup):
#     pass

# """finding price of the accomodation"""
# def getCards(soup, cards = []):
#     for node in soup.find_all("a", {"class": "_93444fe79c--link--eoxce"}):
#         cards.append(node.get('href'))
#     return cards

# print(getCards(soup))

# print(numberOfRooms(soup))

# district = find_district(soup)
# metro_time = time_to_und(soup)
# metro = handy_metro(soup)

# tprint("this works")
# print(metro)
# print(district, metro_time, sep="-----------------------------")



# mydivs = soup.find_all("div", {"class": "_93444fe79c--link--NQlVc"})
# print(mydivs)
# mydivs = soup.find_all("div", {"class": "stylelistrow"})
# district = []

# for node in soup.find_all("div", {"class": "_93444fe79c--labels--L8WyJ"}):
#     district.append(node.findAll(text=True))
#     # print(''.join(node.findAll(text=True)))

# # print(district)
# d = list()

# for _ in range(len(district)):
#     d.append(district[_][2])

# print(len(d))
