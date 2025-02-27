import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-z]', re.IGNORECASE)
    letters = pattern.findall(string)
    palindromes = set()
    for i in range(4, min(len(letters), 7)):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes