import re

def palindromes_of_specific_lengths(string):
    substring = string[14:91]
    pattern = '^(?i)(?P<palindrome>\\\\w{55,71})(?P=palindrome)$'
    matches = re.findall(pattern, substring)
    return set(matches)