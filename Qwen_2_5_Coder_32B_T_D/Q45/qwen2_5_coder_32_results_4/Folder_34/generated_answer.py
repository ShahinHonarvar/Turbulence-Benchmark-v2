from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    s = s[5:8].lower()
    c = Counter(s)
    usable_letters = ''.join([char * (c[char] // 2) for char in string.ascii_lowercase if c[char] > 1])
    palindromes = set()
    for perm in permutations(usable_letters):
        half = ''.join(perm)
        full = half + (c[min(usable_letters, key=lambda x: c[x] % 2)] if any((c[char] % 2 for char in usable_letters)) else '') + half[::-1]
        if len(full) >= 4:
            palindromes.add(full)
    return palindromes