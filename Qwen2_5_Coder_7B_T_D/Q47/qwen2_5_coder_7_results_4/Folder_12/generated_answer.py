import re

def palindromes_of_specific_lengths(s):
    substring = s[62:89].lower()
    pattern = '[a-z]{18,21}'
    palindromes = set()
    for match in re.finditer(pattern, substring):
        if match.group() == match.group()[::-1]:
            palindromes.add(match.group())
    return palindromes