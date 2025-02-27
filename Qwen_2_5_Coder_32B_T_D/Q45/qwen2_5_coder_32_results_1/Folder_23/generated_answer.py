from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    unique_letters = set(letters)
    palindromes = set()
    max_length = 6
    for length in range(4, max_length + 1, 2):
        for perm in permutations(letters, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes