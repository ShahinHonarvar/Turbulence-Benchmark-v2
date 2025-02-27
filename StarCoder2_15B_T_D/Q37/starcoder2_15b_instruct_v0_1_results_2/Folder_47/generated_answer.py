import re

def filter_chars(string):
    pattern = ':[a-qA-Q]+'
    matches = re.findall(pattern, string)
    filtered_string = re.sub(pattern, '', string)
    return filtered_string