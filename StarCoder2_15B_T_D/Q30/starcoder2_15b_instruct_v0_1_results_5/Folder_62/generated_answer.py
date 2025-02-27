import re

def insert_before_character(text: str) -> str:
    """
    Inserts a character before another character in a string.
    """
    return re.sub(' ', 'o ', text)