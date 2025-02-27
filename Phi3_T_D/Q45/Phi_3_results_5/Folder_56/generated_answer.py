from itertools import permutations

def palindromes_between_indices(s):
    target_chars = set(s[5:10].lower())
    valid_palindromes = set()
    for perm in permutations(target_chars, 5):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        valid_palindromes.add(palindrome)
    return valid_palindromes