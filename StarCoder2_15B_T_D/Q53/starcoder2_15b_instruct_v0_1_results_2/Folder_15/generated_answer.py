import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b(?=((\\w)\\2{3,}\\2)(\\2{3,}\\2)*)\\1\\b'
    return set(re.findall(pattern, string, flags=re.IGNORECASE))