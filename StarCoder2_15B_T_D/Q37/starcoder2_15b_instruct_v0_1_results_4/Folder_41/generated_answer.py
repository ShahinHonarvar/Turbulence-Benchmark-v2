import re

def filter_chars(string):
    return re.sub('(?<=26)[V-o](?=64)', '', string)