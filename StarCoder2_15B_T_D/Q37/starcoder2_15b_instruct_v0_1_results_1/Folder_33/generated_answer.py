import re

def filter_chars(string):
    pattern = '[K-m]'
    filtered_string = re.sub(pattern, '', string)
    return filtered_string