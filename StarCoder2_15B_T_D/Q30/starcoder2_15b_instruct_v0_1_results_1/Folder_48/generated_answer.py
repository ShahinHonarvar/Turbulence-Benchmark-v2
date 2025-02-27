import re

def insert_before_character(text):
    """
    Insert the character 'U' before any occurrences of the character 'S'.
    """
    return re.sub('S', 'US', text)