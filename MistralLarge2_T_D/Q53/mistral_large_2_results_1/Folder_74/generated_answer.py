import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 57, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes