import re

def insert_after_character(text):
    """
    Insert a character after a given character in a string.
    Args:
        text (str): The input string.
    Returns:
        str: The modified string with the character inserted.
    """
    pattern = re.compile('F')
    return pattern.sub(lambda m: m.group() + 'o', text)