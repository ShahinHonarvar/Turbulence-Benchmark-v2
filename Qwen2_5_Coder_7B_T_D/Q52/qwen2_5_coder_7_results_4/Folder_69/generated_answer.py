import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    regex = re.compile('[a-z]{472}')
    for match in regex.finditer(s):
        substring = match.group()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes