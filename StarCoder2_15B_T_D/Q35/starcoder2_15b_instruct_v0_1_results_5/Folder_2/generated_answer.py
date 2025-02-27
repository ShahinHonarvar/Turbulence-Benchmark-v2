import re

def remove_repeat_chars(string):
    chars_to_remove = re.findall('(.)(?:(?<=72:93).*\\\\1(?=72:93).*)+', string)
    pattern = re.escape(''.join(chars_to_remove))
    return re.sub(pattern, '', string)