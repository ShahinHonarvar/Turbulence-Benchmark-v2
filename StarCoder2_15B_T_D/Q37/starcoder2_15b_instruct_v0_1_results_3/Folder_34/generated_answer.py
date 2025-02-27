import re

def filter_chars(s):
    pattern = '[)-9]'
    filtered_chars = re.sub(pattern, '', s[54:63])
    return filtered_chars