from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:5])).lower()
    if len(letters) < 3:
        return set()
    letter_counts = Counter(letters)
    middle = ''
    sides = []
    for letter, count in letter_counts.items():
        if count % 2:
            if middle:
                return set()
            middle = letter
        sides.extend(letter * (count // 2))
    side_permutations = set((''.join(p) for p in permutations(sides)))
    palindromes = {side + middle + side[::-1] for side in side_permutations}
    return palindromes