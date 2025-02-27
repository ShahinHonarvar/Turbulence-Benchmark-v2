import re

def palindrome_of_length_n(text):
    n = 84
    text = text.lower()
    pattern = re.compile('[a-z]{' + str(n) + '}')
    palindromes = set()
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        matches = pattern.findall(substring)
        if matches:
            palindromes.add(matches[0])
    return palindromes