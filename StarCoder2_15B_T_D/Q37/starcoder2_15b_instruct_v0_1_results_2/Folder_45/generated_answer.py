import re

def filter_chars(string):
    pattern = re.compile('[\\\\.-b]')
    return pattern.sub('', string)