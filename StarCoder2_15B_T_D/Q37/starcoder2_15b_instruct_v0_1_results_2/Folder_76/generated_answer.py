import re

def filter_chars(text):
    pattern = '[M-v]'
    filtered_text = re.sub(pattern, '', text[379:899])
    return filtered_text