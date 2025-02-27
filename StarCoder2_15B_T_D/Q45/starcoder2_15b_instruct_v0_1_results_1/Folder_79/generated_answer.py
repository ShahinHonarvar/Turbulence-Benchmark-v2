import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 2, 8):
            palindrome = letters[i:j + 1][::-1]
            if palindrome == letters[i:j + 1]:
                palindromes.add(''.join(palindrome).lower())
    return palindromes