import re

def insert_before_character(input_string: str) -> str:
    return re.sub('u', 'U', input_string)