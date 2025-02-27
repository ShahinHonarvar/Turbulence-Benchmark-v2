import re

def return_vowels(text):
    pattern = '[&a-h]'
    result = re.findall(pattern, text[483:664])
    return result