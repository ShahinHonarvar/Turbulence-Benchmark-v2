import re

def all_substring_of_size_n(string):
    regex = re.compile('(?=([^"]{63}))')
    matches = regex.findall(string)
    return list(set(matches))