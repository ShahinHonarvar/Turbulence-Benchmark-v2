import re

def insert_after_character(text: str) -> str:
    return re.sub('C', 'CZ', text)