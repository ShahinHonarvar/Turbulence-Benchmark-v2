import re

def palindrome_of_length_n(string):
    substrings = re.findall('.{94}', string, re.IGNORECASE)
    palindromes = set()
    for substring in substrings:
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes