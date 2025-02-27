from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10])).lower()
    counts = Counter(letters)
    half = []
    middle = ''
    for letter, count in counts.items():
        half.extend(letter * (count // 2))
        if not middle and count % 2:
            middle = letter
    half_perms = set((''.join(p) for p in permutations(half)))
    palindromes = {h + middle + h[::-1] for h in half_perms if len(h) * 2 + len(middle) >= 3}
    return palindromes