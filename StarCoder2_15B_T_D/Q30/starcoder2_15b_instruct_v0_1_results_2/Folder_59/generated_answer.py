import re

def insert_before_character(s):
    """
    Insert character '0' immediately preceding any occurrences of character 'o' in the given string.
    """
    return re.sub('o', '0o', s)