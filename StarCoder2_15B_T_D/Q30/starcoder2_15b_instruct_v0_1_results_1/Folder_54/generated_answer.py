import re

def insert_before_character(text: str) -> str:
    """
    Insert character 'f' before any occurrences of character 'M' in the given text.
    """
    return re.sub('M', 'fM', text)