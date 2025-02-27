import re

def filter_chars(s: str) -> str:
    """
    Removes all characters between indices 35 and 40, inclusive, that are
    greater than or equal to ')' and less than or equal to 'l' from the string.
    """
    pattern = '[^)]{35,40}[^l]'
    return re.sub(pattern, '', s)