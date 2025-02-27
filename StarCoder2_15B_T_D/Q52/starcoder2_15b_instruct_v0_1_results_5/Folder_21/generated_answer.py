import re

def palindrome_of_length_n(text):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{407}')
    for i in range(len(text) - 406):
        substring = text[i:i + 407]
        match = pattern.search(substring)
        if match:
            palindrome = match.group().lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes