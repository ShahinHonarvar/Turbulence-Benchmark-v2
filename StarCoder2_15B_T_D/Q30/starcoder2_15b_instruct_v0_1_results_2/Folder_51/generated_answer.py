import re

def insert_before_character(string):
    return re.sub('o', 'Oo', string)