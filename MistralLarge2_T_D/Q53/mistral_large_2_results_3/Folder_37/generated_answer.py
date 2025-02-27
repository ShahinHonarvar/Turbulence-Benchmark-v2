import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 67, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[A-Za-z]*$', substring):
                palindromes.add(substring.lower())
    return palindromes