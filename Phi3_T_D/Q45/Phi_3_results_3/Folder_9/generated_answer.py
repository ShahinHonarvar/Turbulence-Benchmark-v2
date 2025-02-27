from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:7].lower()
    unique_letters = set(s)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for p in set(permutations(unique_letters, 7)):
        palindrome_candidate = ''.join(p)
        if is_palindrome(palindrome_candidate):
            palindromes.add(palindrome_candidate)
    return palindromes