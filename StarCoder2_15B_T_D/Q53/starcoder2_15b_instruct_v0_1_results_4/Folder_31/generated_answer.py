import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.finditer(pattern, string, flags=re.IGNORECASE):
        word = match.group()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes