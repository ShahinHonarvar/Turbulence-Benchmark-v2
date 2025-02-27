import re

def insert_before_character(input_string):
    """
    Insert a character before another character in a string.
    """
    return re.sub('i', 'ii', input_string)