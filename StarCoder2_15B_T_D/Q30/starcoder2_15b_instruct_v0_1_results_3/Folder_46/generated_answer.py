import re

def insert_before_character(input_string: str) -> str:
    pattern = '6'
    return re.sub(pattern, 'W6', input_string)