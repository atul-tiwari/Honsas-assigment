import re


def pack(name):
    new_string = re.sub('[^A-z0-9 -]', '', name).lower()
    f_string = ""
    for i in new_string.split(" "):
        if i.isdigit():
            f_string += i
        else:
            f_string += (i + " ")

    for word in f_string.split(" "):
        if word.endswith("g") or word.endswith("ml"):
            if word[0].isdigit():
                return word

    return "null"
