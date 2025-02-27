import re

def insert_before_character(string):
    """
    Insert character 'h' immediately preceding any occurrences of character 'o'.
    """
    return re.sub('o', 'ho', string)