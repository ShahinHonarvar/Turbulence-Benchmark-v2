import re

def all_substring_of_size_n(string):
    pattern = re.compile('\\\\b[a-zA-Z0-9]{17}\\\\b')
    substrings = pattern.findall(string)
    return list(set(substrings))