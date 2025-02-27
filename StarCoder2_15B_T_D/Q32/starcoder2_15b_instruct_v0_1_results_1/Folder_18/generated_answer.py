import re

def insert_after_character(string: str) -> str:
    """
    Inserts the character 'l' immediately succeeding any occurrences of the character 'K' in the given string.
    """
    pattern = 'K'
    replacement = 'Kl'
    return re.sub(pattern, replacement, string)