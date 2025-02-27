import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    regex = re.compile('[a-z]{26,29}')
    palindromes = set()
    for match in regex.finditer(s):
        sub = match.group()
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes