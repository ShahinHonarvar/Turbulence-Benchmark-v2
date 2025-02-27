import re

def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    pattern = re.compile('[a-z]{4,5}')
    for match in pattern.finditer(s):
        word = match.group()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes