import re

def remove_repeat_chars(text):
    chars = [c for c in text[2:7]]
    pattern = re.compile('[' + ''.join(chars) + ']+')
    return pattern.sub('', text)