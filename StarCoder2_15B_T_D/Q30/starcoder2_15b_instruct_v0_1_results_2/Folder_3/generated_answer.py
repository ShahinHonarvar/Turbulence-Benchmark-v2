import re

def insert_before_character(string: str) -> str:
    return re.sub('0', 'H0', string)