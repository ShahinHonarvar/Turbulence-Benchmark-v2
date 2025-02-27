import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 98
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes