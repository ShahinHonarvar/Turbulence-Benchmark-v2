import re

def remove_repeat_chars(string):
    chars = set()
    pattern = re.compile('(.)(?=.*\\\\1)')
    string = pattern.sub(lambda m: chars.add(m.group(1)) or '', string[45:48])
    return string