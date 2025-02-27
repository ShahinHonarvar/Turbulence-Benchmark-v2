import re

def palindrome_of_length_at_least_n(s):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.finditer(pattern, s, re.IGNORECASE):
        word = match.group()
        if word.lower() == word[::-1]:
            palindromes.add(word)
    return palindromes