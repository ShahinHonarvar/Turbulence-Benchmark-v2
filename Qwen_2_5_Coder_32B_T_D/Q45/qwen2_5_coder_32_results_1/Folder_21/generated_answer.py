from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:9] if c.isalpha()))
    letter_count = Counter(letters)
    half = []
    middle = ''
    for letter, count in letter_count.items():
        half.extend(letter * (count // 2))
        if count % 2 == 1 and (not middle):
            middle = letter
    half_palindromes = set((''.join(p) for p in permutations(half)))
    palindromes = {h + middle + h[::-1] for h in half_palindromes if len(h + middle + h[::-1]) >= 7}
    return palindromes