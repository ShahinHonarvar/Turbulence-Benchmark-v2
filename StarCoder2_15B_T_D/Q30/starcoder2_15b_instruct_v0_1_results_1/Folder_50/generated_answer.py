import re

def insert_before_character(string: str) -> str:
    pattern = 't'
    replacement = 'ut'
    return re.sub(pattern, replacement, string)