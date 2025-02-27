import re

def palindromes_of_specific_lengths(s):
    subset = s[18:99].lower()
    pattern = re.compile('[a-z]{31,51}')
    matches = pattern.findall(subset)
    palindromes = {word for word in matches if word == word[::-1]}
    return palindromes