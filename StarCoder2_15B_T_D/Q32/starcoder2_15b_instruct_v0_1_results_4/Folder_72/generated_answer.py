import re

def insert_after_character(string):
    pattern = re.compile('O')
    return pattern.sub('Od', string)