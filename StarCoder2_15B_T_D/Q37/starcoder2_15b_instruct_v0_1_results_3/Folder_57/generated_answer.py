import re

def filter_chars(text):
    pattern = '[!-B]'
    result = re.sub(pattern, '', text)
    return result