import re

def palindromes_between_indices(s):
    pattern = '[a-z]{3,}'
    matches = re.finditer(pattern, s, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        start, end = match.span()
        if 5 <= start <= 7 and 5 <= end <= 7:
            palindromes.add(match.group())
    return palindromes