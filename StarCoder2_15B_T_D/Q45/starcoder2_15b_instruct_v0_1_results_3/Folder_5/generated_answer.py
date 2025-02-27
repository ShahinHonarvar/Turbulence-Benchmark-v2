import re

def palindromes_between_indices(text):
    pattern = re.compile('[a-z]', re.IGNORECASE)
    letters = pattern.findall(text[4:9])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes