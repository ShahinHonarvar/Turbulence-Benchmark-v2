import re

def insert_after_character(string: str) -> str:
    return re.sub('0', '0H', string)