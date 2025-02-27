from itertools import permutations

def is_valid_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substr = s[5:8]
    letters = ''.join(sorted(set(substr), key=substr.index))
    palindromes = {permutation.lower() for i in range(4, len(substr) + 1) for permutation in permutations(letters, i) if is_valid_palindrome(''.join(permutation))}
    return palindromes