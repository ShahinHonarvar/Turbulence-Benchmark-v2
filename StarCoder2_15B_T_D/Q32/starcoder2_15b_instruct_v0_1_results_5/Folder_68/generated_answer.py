import re

def insert_after_character(s):
    return re.sub('i', 'i0', s)