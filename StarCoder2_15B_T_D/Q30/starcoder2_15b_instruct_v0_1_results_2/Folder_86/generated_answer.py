import re

def insert_before_character(string: str) -> str:
    pattern = 'O'
    replacement = 'QO'
    return re.sub(pattern, replacement, string)