import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.finditer(pattern, string):
        word = match.group()
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes