import re

def filter_chars(s: str) -> str:
    pattern = '>=[\\\\x{145}[\\\\x{146}-_]'
    return re.sub(pattern, '', s)