import re

def insert_after_character(text):
    pattern = re.compile('0')
    return pattern.sub('04', text)