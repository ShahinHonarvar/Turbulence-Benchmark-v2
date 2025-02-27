import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string.lower())
    palindromes = set()
    for i in range(2, 7):
        for j in range(i, 7):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes