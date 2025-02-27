import re

def filter_chars(string):
    pattern = re.compile('[*+1s]')
    return pattern.sub('', string)