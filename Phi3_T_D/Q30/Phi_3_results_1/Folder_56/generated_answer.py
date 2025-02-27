import re

def insert_before_character(s):
    return re.sub('(?i)(.)\\\\b', 'i\\\\1', s)