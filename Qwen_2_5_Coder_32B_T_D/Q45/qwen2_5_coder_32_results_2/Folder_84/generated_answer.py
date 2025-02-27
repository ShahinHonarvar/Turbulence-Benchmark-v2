from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    letter_counts = Counter(letters)
    mid = ''
    sides = []
    for letter, count in letter_counts.items():
        if count % 2 == 1 and (not mid):
            mid = letter
        sides.append(letter * (count // 2))
    side = ''.join(sides)
    perms = set((''.join(p) for p in permutations(side)))
    palindromes = {s + mid + s[::-1] for s in perms if len(s + mid + s[::-1]) >= 3}
    return palindromes