import re

def insert_after_character(string):
    """
    Insert a character after another character in a string.
    """
    return re.sub('g', 'gt', string)