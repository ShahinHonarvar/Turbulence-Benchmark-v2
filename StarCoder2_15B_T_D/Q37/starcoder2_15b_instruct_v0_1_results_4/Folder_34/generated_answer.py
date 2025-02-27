import re

def filter_chars(s):
    s = re.sub('[())-9]{6}', '', s)
    return s