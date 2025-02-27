import re

def insert_before_character(input_string):
    return re.sub('HC', 'HHC', input_string)