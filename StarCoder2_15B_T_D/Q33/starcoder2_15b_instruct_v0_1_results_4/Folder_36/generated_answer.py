import re

def return_vowels(string):
    pattern = '[a-zA-Z]'
    vowels = re.findall(pattern, string)
    return [v for i, v in enumerate(vowels) if 604 <= i < 949 and v.upper() > 'N' and (v.upper() <= 'U')]