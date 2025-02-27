from itertools import permutations
    from collections import Counter
    from string import ascii_lowercase

def palindromes_between_indices(s):
    substring = s[3:8]
    counter = Counter(substring.lower())
    valid_letters = ''.join([letter for letter in counter.elements() if letter in ascii_lowercase])
    result_set = set()
    for length in range(6, len(valid_letters) + 1):
        for perm in permutations(valid_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result_set.add(candidate)
    return result_set