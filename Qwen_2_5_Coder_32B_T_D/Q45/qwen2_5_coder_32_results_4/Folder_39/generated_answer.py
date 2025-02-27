from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:6])).lower()
    count = Counter(letters)
    half = []
    middle = ''
    for letter, freq in count.items():
        half.extend(letter * (freq // 2))
        if freq % 2 == 1 and (not middle):
            middle = letter
    half_permutations = set((''.join(p) for p in permutations(half)))
    return {h + middle + h[::-1] for h in half_permutations if len(h + middle + h[::-1]) >= 3}