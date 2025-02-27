import re

def insert_after_character(string: str) -> str:
    return re.sub('B', 'BN', string)