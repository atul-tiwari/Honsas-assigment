from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

URL = "https://mamaearth.in/product/charcoal-facial-regimen-kit"


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('verbose')
options.add_argument('log-level=3')


wd = webdriver.Chrome(options=options)
wd.get(URL)

WebDriverWait(wd, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "woodmart-list")))

# And grab the page HTML source
html_page = wd.page_source
wd.quit()

# Now you can use html_page as you like
soup = BeautifulSoup(html_page, 'lxml')

_ingredient = []

coll_data = soup.find(
    class_="woodmart-list").find_all("strong")

for i in coll_data:
    _text = i.text[:i.text.find(':')]
    _ingredient.append(_text.strip().lower())

print(_ingredient)
