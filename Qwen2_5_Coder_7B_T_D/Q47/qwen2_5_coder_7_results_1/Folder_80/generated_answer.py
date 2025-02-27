import re

def palindromes_of_specific_lengths(s):
    substring = s[35:89].lower()
    pattern = re.compile('[a-z]{24,33}')
    palindromes = set()
    for match in pattern.finditer(substring):
        candidate = match.group()
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes