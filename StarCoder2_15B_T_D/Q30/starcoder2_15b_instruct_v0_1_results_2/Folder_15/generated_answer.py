import re

def insert_before_character(input_string):
    return re.sub('o', 'o o', input_string)