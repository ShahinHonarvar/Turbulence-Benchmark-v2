import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + 89, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes