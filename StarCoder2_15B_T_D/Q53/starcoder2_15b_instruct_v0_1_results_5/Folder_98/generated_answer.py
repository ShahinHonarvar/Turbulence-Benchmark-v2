import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{6,}'
    matches = re.finditer(pattern, string)
    for match in matches:
        word = match.group()
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes