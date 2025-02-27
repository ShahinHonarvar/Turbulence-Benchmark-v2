import re

def remove_repeat_chars(string):
    pattern = '(.)\\\\1'
    return re.sub(pattern, '', string[55:84])