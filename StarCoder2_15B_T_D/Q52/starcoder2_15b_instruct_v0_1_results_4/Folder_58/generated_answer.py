import re

def palindrome_of_length_n(text):
    regex = re.compile('(?i)(\\w{223})(?=\\1)')
    matches = regex.findall(text)
    return set(matches)