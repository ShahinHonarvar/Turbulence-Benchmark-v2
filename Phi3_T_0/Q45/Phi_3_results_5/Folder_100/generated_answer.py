from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(6, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes