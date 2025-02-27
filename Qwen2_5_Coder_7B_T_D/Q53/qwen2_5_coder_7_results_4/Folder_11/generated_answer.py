import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 53):
        for j in range(54, len(s) - i + 1):
            substring = s[i:i + j]
            if substring == substring[::-1] and re.match('^[a-z]*$', substring):
                palindromes.add(substring)
    return palindromes