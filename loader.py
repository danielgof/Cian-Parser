import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""класс, отвечающий за загрузку данных"""
class Loader:
    """Загрузка страниц с сайта"""
    def loadPages():
        if not os.path.exists("pages_html"):
            os.mkdir("pages_html")
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe")
        for page in range(2):
            driver.get(f"https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&foot_min=30&offer_type=flat&only_foot=2&p={page + 1}&region=1&room1=1&room2=1&room3=1&sort=price_object_order")
            with open(f"pages_html\data{page + 1}.html", mode='a', encoding='utf-8') as file:
                file.write(driver.page_source)
        driver.quit()
        pages = os.listdir("pages_html")
        return pages


    """Загрузка карточкек с объявлениями по сайту"""
    def loadCards(pages, cards = [], pgs = []):
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe")
        if not os.path.exists(f"cards"):
            os.mkdir(f"cards")
        for page in pages:
            # print(os.getcwd())
            with open(f"./pages_html/{page}", "r", encoding='utf-8') as f:
                text = f.read()
            soup = BeautifulSoup(text, features="lxml")
            for node in soup.find_all("a", {"class": "_93444fe79c--link--eoxce"}):
                cards.append(node.get('href'))
            # print(cards)
            if not os.path.exists(f"cards/{page[:6:]}"):
                os.mkdir(f"cards/{page[:6:]}")
            os.chdir(f"cards/{page[:6:]}")
            # print(os.getcwd())
            for card in cards:
                driver.get(card)
                with open(f"{card[-9:-1:]}.html", mode='a', encoding='utf-8') as file:
                    file.write(driver.page_source)
            pgs.append(os.listdir())
            os.chdir("../..")
        return pgs

# pages = ['data1.html']
# pages = Loader.loadPages()
# cards = Loader.loadCards(pages)
# print(cards)