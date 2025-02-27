import re

def filter_chars(string):
    pattern = '[K-z]'
    filtered_string = re.sub(pattern, '', string[29:80])
    return filtered_string