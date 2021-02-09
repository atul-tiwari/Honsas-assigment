from bs4 import BeautifulSoup
from selenium import webdriver


class Product_Data:

    def __init__(self, product_link=""):
        super().__init__()
        baseURL = "https://mamaearth.in"

        self.link = baseURL+product_link

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(3000)

        browser.get(self.link)
        browser.execute_script("return document.readyState")

        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')

        data_Div = soup.find(
            class_="ProductDetails__Wrapper-sc-1htzzsm-0 fXidSC")

        print(data_Div.find("h1").text)
        print(data_Div.find(
            "div", class_="Flex-sc-1lsr9yp-0 egCJRE ReviewBox").find("span").text)
        print(data_Div.find("div", class_="price").text)
        temp = data_Div.find("div", class_="price__discount")
        print(temp.text if temp != None else "0%")

        print(data_Div.find(class_="Description-sc-40bbdp-0 gwjNeT").find_all("span"))

        coll_data = soup.find(class_="woodmart-list").find_all("strong")
        print(coll_data)


p1 = Product_Data(
    "/product/charcoal-face-wash-scrub-combo")
