import re

def insert_after_character(text: str) -> str:
    """
    Inserts the character 'U' after any occurrences of the character 'u'.
    """
    return re.sub('u', 'uU', text)