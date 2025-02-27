from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[2:9]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    letters = ''.join(set(substring))
    palindromes = set()
    for i in range(7, len(substring) + 1):
        for p in permutations(letters, i):
            s = ''.join(p)
            if is_palindrome(s):
                palindromes.add(s)
    return palindromes