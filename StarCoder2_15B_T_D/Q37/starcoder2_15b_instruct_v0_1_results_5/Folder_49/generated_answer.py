import re

def filter_chars(s: str) -> str:
    pattern = re.compile('(?<=42\\\\d*)[*+](?=97\\\\d*)')
    result = pattern.sub('', s)
    return result