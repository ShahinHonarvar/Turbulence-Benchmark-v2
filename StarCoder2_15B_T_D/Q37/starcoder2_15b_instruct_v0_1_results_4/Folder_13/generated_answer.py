import re

def filter_chars(string):
    return ''.join([c for c in string if not re.match('[9-s]', c)])