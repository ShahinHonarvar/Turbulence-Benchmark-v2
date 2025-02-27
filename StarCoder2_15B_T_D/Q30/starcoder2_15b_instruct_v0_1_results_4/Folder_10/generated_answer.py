import re

def insert_before_character(string):
    """
    Insert a character before another character in a string.
    """
    return re.sub('j', 'vj', string)