import re

def insert_before_character(text: str) -> str:
    """
    Inserts 'T' before any occurrences of 'E' in the given text.
    """
    pattern = re.compile('E')
    return pattern.sub(lambda m: 'TE', text)