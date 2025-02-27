from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[5:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in set(permutations(letters, length)):
            if is_palindrome(''.join(p)):
                palindromes.add(''.join(p))
    return palindromes