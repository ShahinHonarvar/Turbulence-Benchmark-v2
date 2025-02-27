from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10]
    letters = [char for char in substring if char.isalpha()]
    palindrome_set = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 5:
            palindrome_set.add(candidate)
    return palindrome_set