import re

def insert_before_character(string: str) -> str:
    return re.sub('U', 'FU', string)