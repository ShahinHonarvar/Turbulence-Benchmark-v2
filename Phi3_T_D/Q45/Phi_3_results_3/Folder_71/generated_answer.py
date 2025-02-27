import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    unique_letters = set(letters)
    result = set()
    for length in range(4, len(unique_letters) + 1):
        for subset in itertools.permutations(unique_letters, length):
            candidate = ''.join(subset)
            if is_palindrome(candidate):
                result.add(candidate)
    return result