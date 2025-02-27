from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[0:6].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        for i in range(len(letters) - 5):
            candidate = ''.join(perm[i:i + 6])
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes