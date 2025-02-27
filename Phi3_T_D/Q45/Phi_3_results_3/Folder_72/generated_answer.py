from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[1:8].lower()
    char_data = Counter(s)
    all_permutations = [''.join(p) for p in permutations(s, len(s)) if all((char_data[char] >= p.count(char) for char in p))]
    return set(filter(lambda x: x == x[::-1] and len(x) >= 6, all_permutations))