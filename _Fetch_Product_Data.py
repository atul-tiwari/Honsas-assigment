from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


# ihis class featch the data from the product page
class Product_Data:

    def fetchName(self):
        self.name = self._data_Div.find("h1").text

    def fetchRating(self):
        rate = self._data_Div.find(
            "div", class_="Flex-sc-1lsr9yp-0 egCJRE ReviewBox").find("span").text

        self.rating = float(rate[1:-1])

    def fetchPrice(self):
        self.price = float((self._data_Div.find(
            "div", class_="price").text[1:]).replace(",", ""))

    def fetchDiscount(self):
        temp = self. _data_Div.find("div", class_="price__discount")
        if temp != None:
            self.discount = (temp.text[1:-1].split(' ')[0])
        else:
            self.discount = "0%"

    def fetchDiscription(self):
        paragraph = (self._data_Div.find(
            class_="Description-sc-40bbdp-0 gwjNeT").find_all("span"))

        dis = self.name
        for p in paragraph:
            dis += p.text

        self.discription = dis

    def fetchIngredients(self):

        _ingredient = []

        coll_data = self._soup.find(
            class_="woodmart-list").find_all("strong")

        for i in coll_data:
            _text = i.text[:i.text.find(':')]
            _ingredient.append(_text.strip().lower())

        self.ingredients = _ingredient

    def featchPack(self):
        new_string = re.sub('[^A-z0-9 -]', '', self.name).lower()
        f_string = ""
        for i in new_string.split(" "):
            if i.isdigit():
                f_string += i
            else:
                f_string += (i + " ")

        for word in f_string.split(" "):
            if word.endswith("g") or word.endswith("ml"):
                if word[0].isdigit():
                    return word

        return "null"

    def __init__(self, product_link=""):
        super().__init__()
        baseURL = "https://mamaearth.in"

        self.link = baseURL+product_link

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('verbose')
        options.add_argument('log-level=3')

        browser = webdriver.Chrome(options=options)

        browser.get(self.link)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "woodmart-list")))

        html = browser.page_source
        browser.quit()

        self._soup = BeautifulSoup(html, 'lxml')

        self._data_Div = self._soup.find(
            class_="ProductDetails__Wrapper-sc-1htzzsm-0 fXidSC")

        self.fetchRating()
        self.fetchName()
        self.fetchPrice()
        self.fetchDiscount()
        self.fetchDiscription()
        self.fetchIngredients()
        self.size = self.featchPack()

        print("Done  "+self.name+"\n\n")

#
