import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import Get_Key_ingredients
import Get_Category


# Get key ingredients
dt = pd.read_csv('Raw_Data.csv')

names = list(dt['Name'])
ingredients = list(dt['Ingredients'])

key_ingredients = Get_Key_ingredients.calculate_key_ingredients(
    names, ingredients)


# get the Doc init the Vectorizer

data = list(dt['Discription'])
document = list(map(Get_Category.cleanString, data))
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(document)

# GET Model

loaded_model = pickle.load(open("Final_model", 'rb'))
clusters = ["Face Product", "Hair Product", "Skin Product"]


# Get Predictions
products = list(map(Get_Category.cleanString, names))
p_data = vectorizer.transform(products)

pred = loaded_model.predict(p_data)

# wrighting data into csv


def cluster_name(x): return clusters[x]


result = {
    'Product Name ': map(Get_Category.cleanString, names),
    'Key Ingredient': key_ingredients,
    'Category': map(cluster_name, pred)
}

df = pd.DataFrame(result)

# saving the dataframe
df.to_csv('Results.csv', index=False)
