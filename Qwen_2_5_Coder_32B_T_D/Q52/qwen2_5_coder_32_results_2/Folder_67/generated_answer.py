import re

def palindrome_of_length_n(s):
    s = s.lower()
    regex = re.compile('(?=[a-z]{' + str(42) + '})')
    palindromes = set()
    for match in regex.finditer(s):
        sub = s[match.start():match.start() + 42]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes