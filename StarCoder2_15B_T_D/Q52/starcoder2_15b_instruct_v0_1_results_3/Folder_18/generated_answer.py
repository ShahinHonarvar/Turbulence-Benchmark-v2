import re

def palindrome_of_length_n(string):
    pattern = re.compile('(^|\\b)(?P<palindrome>\\w{392})(?=\\1)', re.IGNORECASE)
    return set((match.group('palindrome') for match in pattern.finditer(string)))