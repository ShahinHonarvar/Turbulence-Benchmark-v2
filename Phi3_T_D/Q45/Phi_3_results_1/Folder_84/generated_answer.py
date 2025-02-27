from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    subset = s[3:10].lower()
    letters = ''.join(sorted((char for char in subset if char.isalpha())))
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes