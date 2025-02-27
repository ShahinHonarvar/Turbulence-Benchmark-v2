from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    counter = Counter(substring.lower())
    center = ''
    left_right = ''
    for char, count in counter.items():
        if char.isalpha():
            left_right += char * (count // 2)
            if count % 2 != 0 and center == '':
                center = char
    if len(left_right) < 2:
        return set()
    half_palindromes = [''.join(p) for p in set(permutations(left_right, 2))]
    palindromes = set()
    for half in half_palindromes:
        palindromes.add(half + (center if center else '') + half[::-1])
    return palindromes