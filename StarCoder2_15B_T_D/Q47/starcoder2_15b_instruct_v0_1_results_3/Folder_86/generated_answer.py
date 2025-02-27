import re

def palindromes_of_specific_lengths(text):
    pattern = re.compile('[a-zA-Z]{34,55}')
    palindromes = set()
    for match in pattern.finditer(text[30:96]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes