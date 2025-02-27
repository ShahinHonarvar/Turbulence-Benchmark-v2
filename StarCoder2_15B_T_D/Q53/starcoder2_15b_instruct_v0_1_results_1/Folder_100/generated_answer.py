import re

def palindrome_of_length_at_least_n(string: str) -> set:
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.finditer(pattern, string):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes