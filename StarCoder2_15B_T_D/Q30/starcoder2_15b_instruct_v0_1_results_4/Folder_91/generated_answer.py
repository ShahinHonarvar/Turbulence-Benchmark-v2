import re

def insert_before_character(string):
    pattern = re.compile('a')
    return pattern.sub('0a', string)