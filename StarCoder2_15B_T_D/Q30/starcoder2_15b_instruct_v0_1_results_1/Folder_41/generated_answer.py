import re

def insert_before_character(text):
    """
    Insert a character before another character in a string.
    """
    return re.sub('O', 'oO', text)