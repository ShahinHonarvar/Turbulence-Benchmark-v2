import re

def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 32):
        substring = text[i:i + 33]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes