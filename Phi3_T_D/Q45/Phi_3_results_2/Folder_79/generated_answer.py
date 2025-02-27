import itertools
import string

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    length = min(7, len(s))
    palindromes = set()
    c = Counter(s[1:length + 1])
    if sum(c.values()) < 3:
        return palindromes
    for charset in itertools.combinations_with_replacement(c, 3):
        if sum(charset) == length:
            for permutation in itertools.permutations(charset):
                candidate = ''.join(permutation).lower()
                if is_palindrome(candidate):
                    palindromes.add(''.join(sorted(candidate)))
    return palindromes