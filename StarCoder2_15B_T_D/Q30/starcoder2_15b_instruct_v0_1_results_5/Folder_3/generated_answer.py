import re

def insert_before_character(string):
    pattern = '0'
    replacement = 'H0'
    return re.sub(pattern, replacement, string)