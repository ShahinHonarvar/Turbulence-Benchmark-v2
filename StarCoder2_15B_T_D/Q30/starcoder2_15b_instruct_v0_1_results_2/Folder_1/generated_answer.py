import re

def insert_before_character(string):
    """
    Insert 'T' before every occurrence of 'U' in the given string.
    """
    return re.sub('U', 'TU', string)