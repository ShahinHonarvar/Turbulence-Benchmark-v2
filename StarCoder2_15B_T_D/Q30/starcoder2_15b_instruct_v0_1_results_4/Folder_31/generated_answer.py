import re

def insert_before_character(input_string):
    return re.sub('B', 'NB', input_string)