import itertools
from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:9]
    letter_count = Counter(substring.lower())

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for length in range(3, sum(letter_count.values()) + 1):
        possible_chars = [char for char, count in letter_count.items() for _ in range(count)]
        for perm in itertools.permutations(possible_chars, length):
            candidate = ''.join(perm)
            if len(candidate) < length:
                candidate += candidate[:1]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes