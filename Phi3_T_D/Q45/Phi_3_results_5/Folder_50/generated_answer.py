from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    middle = s[4:9].lower()
    length = sum((1 for c in middle if c.isalpha()))
    if length < 5:
        return set()
    palindromes = set()
    for i in range(length, 5, -1):
        if is_palindrome(middle[:i]):
            palindromes.add(middle[:i])
            for perm in permutations(middle[:i]):
                palindrome_candidate = ''.join(perm)
                palindromes.add(palindrome_candidate)
    return palindromes