import re

def palindrome_of_length_n(string):
    pattern = '(?i)(?:(?=(?:(?!(?-i)\\2)\\w)\\3+)(?!\\3))\\w{464}'
    return set(re.findall(pattern, string))