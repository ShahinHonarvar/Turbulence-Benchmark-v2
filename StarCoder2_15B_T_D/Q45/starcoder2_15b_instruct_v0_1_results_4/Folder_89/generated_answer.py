import re

def palindromes_between_indices(s):
    letters = re.findall('[a-z]', s.lower())
    palindromes = set()
    for i in range(5, 10):
        for j in range(i, 10):
            palindrome = letters[i:j + 1] + letters[i:j + 1][::-1]
            palindromes.add(''.join(palindrome))
    return palindromes