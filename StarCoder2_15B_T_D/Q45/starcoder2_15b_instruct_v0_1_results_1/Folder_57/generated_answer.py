import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-z]', re.IGNORECASE)
    letters = pattern.findall(string[2:6])
    palindromes = set()
    for i in range(len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes