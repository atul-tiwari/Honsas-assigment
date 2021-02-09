from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = 'https://mamaearth.in/product-category/beauty'
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

print(type(soup))

results = soup.find(class_="renderProductListData__Wrapper-sc-16np6sh-0 DtsGp")


children = results.findChildren("div", recursive=False)

product_links = []

for child in children:
    product_links.append(child.find(
        "div", class_="uniquewhite").find("div").find("a")['href'])

P_dict = {'Product Links': product_links}

df = pd.DataFrame(P_dict)

# saving the dataframe
df.to_csv('ProductLinks.csv', index=False)
