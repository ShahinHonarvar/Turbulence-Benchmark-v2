import re

def insert_after_character(string: str) -> str:
    """
    Insert character 'y' immediately succeeding any occurrences of character 'b' in a given string.
    """
    return re.sub('b', 'by', string)