from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    char_count = Counter(s[8:10])
    valid_chars = ''.join([c.upper() for c in s[8:10]])
    palindromes = set()
    for length in range(3, len(valid_chars) + 1, 2):
        for p in permutations(valid_chars, length):
            if is_palindrome(''.join(p)):
                palindromes.add(''.join(p).lower())
    return palindromes