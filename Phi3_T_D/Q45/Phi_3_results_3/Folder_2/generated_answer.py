from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6]]
    if len(letters) < 6:
        return set()
    letters_count = Counter(letters)
    palindrome_set = set()

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindrome_set.add(candidate)
    return palindrome_set