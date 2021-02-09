import _Fetch_Product_Data
import pandas as pd
import csv

dt = pd.read_csv('temp.csv')

products = list(dt['Product Links'])

name = []
link = []
rating = []
price = []
discount = []
discription = []
ingredients = []


for item in products:
    obj = _Fetch_Product_Data.Product_Data(item)
    name.append(obj.name)
    link.append(obj.link)
    rating.append(obj.rating)
    price.append(obj.price)
    discount.append(obj.discount)
    discription.append(obj.discription)
    ingredients.append(obj.ingredients)
    del(obj)

P_dict = {
    'Name': name,
    'Link': link,
    'Rating': rating,
    'Price': price,
    'Discount': discount,
    'Ingredients': ingredients,
    'Discription': discription,
}

df = pd.DataFrame(P_dict)

# saving the dataframe
df.to_csv('Raw_Data.csv', index=False)
