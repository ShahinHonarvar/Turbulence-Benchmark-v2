import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(string)
    palindromes = set()
    for i in range(7):
        for j in range(i, 7):
            palindrome = letters[i:j + 1]
            reversed_palindrome = list(palindrome)
            reversed_palindrome.reverse()
            if palindrome == reversed_palindrome:
                palindromes.add(''.join(palindrome))
    return palindromes