import re

def remove_repeat_chars(string):
    chars_to_remove = set(re.findall('(.)(?:.*\\\\1){2}', string[86:90]))
    pattern = re.compile('[' + ''.join(chars_to_remove) + ']')
    return pattern.sub('', string)