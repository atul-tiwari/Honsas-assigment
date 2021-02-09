from bs4 import BeautifulSoup
from selenium import webdriver


class Product_Data:

    def fetchName(self):
        self.name = self._data_Div.find("h1").text

    def fetchRating(self):
        rate = self._data_Div.find(
            "div", class_="Flex-sc-1lsr9yp-0 egCJRE ReviewBox").find("span").text

        self.rating = float(rate[1:-1])

    def fetchPrice(self):
        self.price = float(self._data_Div.find("div", class_="price").text[1:])

    def fetchDiscount(self):
        temp = self. _data_Div.find("div", class_="price__discount")
        if temp != None:
            self.discount = (temp.text[1:-1].split(' ')[0])
        else:
            self.discount = "0%"

    def fetchDiscription(self):
        paragraph = (self._data_Div.find(
            class_="Description-sc-40bbdp-0 gwjNeT").find_all("span"))

        dis = ""
        for p in paragraph:
            dis += p.text

        self.discription = dis

    def fetchIngredients(self):

        try:
            coll_data = self._soup.find(
                class_="woodmart-list").find_all("strong")

            _ingredient = []
            for i in coll_data:
                _text = i.text[:i.text.find(':')]
                _ingredient.append(_text.strip().lower())
        except:
            self._retry += 1
            if self._retry <= 3:
                self.fetchIngredients()
            else:
                print("Error in Fetching Ingredients")
                return

        self.ingredients = _ingredient

    def __init__(self, product_link=""):
        super().__init__()
        baseURL = "https://mamaearth.in"

        self.link = baseURL+product_link
        self._retry = 0
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(3000)

        browser.get(self.link)
        browser.execute_script("return document.readyState")

        html = browser.page_source
        self._soup = BeautifulSoup(html, 'lxml')

        self._data_Div = self._soup.find(
            class_="ProductDetails__Wrapper-sc-1htzzsm-0 fXidSC")

        self.fetchRating()
        self.fetchName()
        self.fetchPrice()
        self.fetchDiscount()
        self.fetchDiscription()
        self.fetchIngredients()
