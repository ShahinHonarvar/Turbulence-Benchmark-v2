import re

def insert_after_character(string):
    """
    Insert character 'a' after any occurrences of character 'U' in a given string.
    """
    pattern = 'U'
    replacement = 'Ua'
    return re.sub(pattern, replacement, string)