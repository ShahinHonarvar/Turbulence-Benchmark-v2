from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7]]
    unique_letters = set(letters)
    palindromes = set()
    for perm in permutations(unique_letters):
        candidate = ''.join(perm)
        if len(candidate) >= 7 and is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes