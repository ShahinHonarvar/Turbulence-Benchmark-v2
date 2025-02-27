import re

def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 81 or i >= 89 or (not (c > 'f' and c < '{'))])