import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('(?<=^.{140,})(.+?)\\1(?=.*$)', re.IGNORECASE)
    return set(pattern.findall(string))