import re

def palindrome_of_length_at_least_n(s):
    pattern = re.compile('[A-Za-z]{52,}')
    return set((m.group() for m in pattern.finditer(s) if m.group().lower() == m.group()[::-1]))