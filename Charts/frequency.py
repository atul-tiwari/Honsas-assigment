import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

res = pd.read_csv("D:\Projects\mamaEarth Assigment\Results.csv")

cat = list(res['Category'])

cat_dict = {
    'Face Product': 0,
    'Skin Product': 0,
    'Hair Product': 0,
}
# creating the dataset
for i in cat:
    cat_dict[i] = (cat_dict[i]+1)

courses = list(cat_dict.keys())
values = list(cat_dict.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, width=0.4)

plt.xlabel("Product Categories")
plt.ylabel("No. of product")
plt.title("Products")
# plt.show()

rawData = pd.read_csv("D:\Projects\mamaEarth Assigment\Raw_Data.csv")

price = list(rawData['Price'])

plt.hist(price)
plt.xlabel("Price")
plt.ylabel("No. of product")
plt.title("Histrogram of price")
plt.show()

ing = list(res['Key Ingredient'])

ing_dict = {}

for j in ing:
    j = j.replace("vitamin c", "vitaminC")
    for i in j.split(' '):
        if i in ing_dict.keys():
            ing_dict[i] += 1
        else:
            ing_dict[i] = 1

top_used_k = []
top_used_v = []
sorted_keys = sorted(ing_dict, key=ing_dict.get, reverse=True)
for r in sorted_keys:
    top_used_k.append(r)
    top_used_v.append(ing_dict[r])

# Horizontal Bar Plot
plt.bar(top_used_k[1:11], top_used_v[1:11])

# Show Plot
plt.xlabel("Key Ingredient")
plt.ylabel("No. of product")
plt.title("Most used Key Ingredient")
plt.show()
print(top_used_v)
