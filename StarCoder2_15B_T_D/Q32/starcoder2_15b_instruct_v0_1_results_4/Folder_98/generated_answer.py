import re

def insert_after_character(string: str) -> str:
    pattern = 'U'
    replacement = 'Uu'
    return re.sub(pattern, replacement, string)