import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(46) + ',}'
    matches = re.finditer(pattern, text)
    for match in matches:
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes