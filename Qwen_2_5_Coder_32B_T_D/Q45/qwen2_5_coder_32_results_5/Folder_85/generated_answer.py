from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:9])).lower()
    counts = Counter(letters)
    half_len = 3
    halfs = set()
    for perm in permutations(letters, half_len):
        half = ''.join(perm)
        if half.count(half[0]) <= counts[half[0]] and half.count(half[1]) <= counts[half[1]] and (half.count(half[2]) <= counts[half[2]]):
            halfs.add(half)
    palindromes = {h + (h[-2::-1] if h[0] == h[-1] else h[::-1]) for h in halfs}
    return palindromes