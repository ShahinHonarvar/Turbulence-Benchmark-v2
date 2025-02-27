import re

def insert_before_character(string):
    """
    Insert character 'a' immediately preceding any occurrences of character 'o'.
    """
    return re.sub('o', 'ao', string)