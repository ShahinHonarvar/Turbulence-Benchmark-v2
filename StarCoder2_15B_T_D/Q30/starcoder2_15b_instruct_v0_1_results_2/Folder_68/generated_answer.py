import re

def insert_before_character(string):
    return re.sub('i', '0i', string)