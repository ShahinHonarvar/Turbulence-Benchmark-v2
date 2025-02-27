import re

def insert_before_character(input_string: str) -> str:
    return re.sub('e', 'Ee', input_string)