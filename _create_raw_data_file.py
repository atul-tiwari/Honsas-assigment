import _Fetch_Product_Data
import pandas as pd
import csv

dt = pd.read_csv('ProductLinks.csv')

products = list(dt['Product Links'])

name = []
link = []
rating = []
price = []
discount = []
discription = []
ingredients = []
pack = []

num = 1
error = 0
er = []

# this will create the Raw data file wich will have all data in it
for item in products:
    print(num)
    try:
        obj = _Fetch_Product_Data.Product_Data(item)
        name.append(obj.name)
        link.append(obj.link)
        rating.append(obj.rating)
        price.append(obj.price)
        discount.append(obj.discount)
        discription.append(obj.discription)
        ingredients.append(obj.ingredients)
        pack.append(obj.size)
        del(obj)
    except:
        print("ERROR : "+item)
        error += 1
        er.append(item)
    num += 1

P_dict = {
    'Name': name,
    'Link': link,
    'Rating': rating,
    'Price': price,
    'Discount': discount,
    'Pack': pack,
    'Ingredients': ingredients,
    'Discription': discription,
}

df = pd.DataFrame(P_dict)

# saving the dataframe
df.to_csv('Raw_Data.csv', index=False)
