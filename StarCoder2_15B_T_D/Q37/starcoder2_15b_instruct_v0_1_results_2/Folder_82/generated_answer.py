import re

def filter_chars(text: str) -> str:
    pattern = '[P-x]'
    return re.sub(pattern, '', text[12:26])