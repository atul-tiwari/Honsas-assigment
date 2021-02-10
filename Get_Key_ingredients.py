import re

# string cleaning removeing unwanted stuff


def compstr(st):
    new_string = re.sub('[^A-z0-9 -]', '', st).lower()
    return new_string

# just check the feached ingredients form page and pick the key ingredient


def calculate_key_ingredients(names, ingredients):
    list_ingredients = []
    main_ingredients = []

    for i in ingredients:
        temp_str = i[1:-1]
        temp_str = temp_str.replace(",", "")
        temp_str = temp_str.replace("'", "")
        li = temp_str.split(" ")
        list_ingredients.append(li)

    for item in range(len(names)):
        li = list_ingredients[item]
        key_ing = []
        for ing in li:
            if ing in compstr(names[item]).split(" ") and ing not in key_ing:
                key_ing.append(ing)
        if key_ing == []:
            main_ingredients.append(li[0])
        else:
            temp_str = ""
            for i in key_ing:
                temp_str += (i+' ')
            main_ingredients.append(temp_str)

    return main_ingredients
