import re

def insert_before_character(string):
    return re.sub('u', 'uu', string)