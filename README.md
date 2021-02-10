# MamaEarth
mamaEarth Assigment

Python lib used are  :-  selenium,BeautifulSoup,sklearn,re,pandas,matplot
### Workbook Link

Link :- Work Book
[MAMAEARTH.xlsx](https://github.com/atul-tiwari/mamaEarth/files/5956793/mamaearth.xlsx)

# how project Works

Step 1 :- Run file '_Fetch_Data.py'  this file will fetch all the product links from the BaseUrl :- 'https://mamaearth.in/product-category/beauty' and store them into an File name 'Productlinks.csv'

Step 2 :- file '_Fetch_Product_Data.py' file will go to each product link and fetch the following info using selenium and BeautifulSoup

  * Name
  * Link
  * Rating
  * Price
  * Discount
  * Pack
  * Ingredients
  * Discription
  
Step 3 :- File '_create_raw_data_file.py' will collect all the data provided by Product Data class and store it ino a file name 'Raw_Data.csv'

Step 4 :- 'Get_Key_Ingredients.py' file waill take take all the ingredients from the 'Rawdata.csv' file and then find the key Ingredients

Step 5 :- 'Get_Category.py' File will train the dataset for the classification of product based upon their Discription.

Step 6 :- 'Get_Result.py' will take all the data and output a file name 'Result.csv' wich only hve three columns 
  * Name
  * key Ingredient
  * Class of product
  
  
# Machine Learning Model

* lib used  :- Sklearn

* Model used :- KMeans

* No of clusters = 3

* Clusters name = "Face Product", "Hair Product", "Skin Product"

* Traning Data = discriptions of all the products

* Preprocessing 
  - remove all numbers and punctuation marks
  - all to lowercase
  - methord used :- TF-IDF Vectorizer
  

#statistics

![Figure_1](https://user-images.githubusercontent.com/24614316/107484856-04da6a00-6ba9-11eb-9982-1e7e5e18674e.png)
![Figure_2](https://user-images.githubusercontent.com/24614316/107484860-060b9700-6ba9-11eb-95e7-2383da6006cf.png)
![Figure_3](https://user-images.githubusercontent.com/24614316/107484863-06a42d80-6ba9-11eb-834d-8a1b8dcdc5a6.png)
