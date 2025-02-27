import re

def insert_before_character(string: str) -> str:
    pattern = re.compile('U')
    result = re.sub(pattern, 'aU', string)
    return result