import re

def insert_after_character(text):
    """
    Insert 'f' after each occurrence of 'M' in the input string.
    """
    return re.sub('M', 'Mf', text)