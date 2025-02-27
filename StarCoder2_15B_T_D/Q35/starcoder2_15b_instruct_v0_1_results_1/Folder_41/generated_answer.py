import re

def remove_repeat_chars(text):
    pattern = '(.)\\\\1'
    return re.sub(pattern, '', text[3:8])