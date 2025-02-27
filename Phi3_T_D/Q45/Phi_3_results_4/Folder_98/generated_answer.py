from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (3, 5)
    letters = s[start:end + 1].lower()
    unique_letters = ''.join(set(letters))
    palindromes = set()
    for perm in permutations(unique_letters, 4):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes