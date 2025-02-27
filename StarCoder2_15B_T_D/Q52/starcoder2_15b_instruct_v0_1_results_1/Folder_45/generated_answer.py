import re

def palindrome_of_length_n(text):
    palindromes = set()
    n = 21
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring == substring[::-1]:
            if re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes