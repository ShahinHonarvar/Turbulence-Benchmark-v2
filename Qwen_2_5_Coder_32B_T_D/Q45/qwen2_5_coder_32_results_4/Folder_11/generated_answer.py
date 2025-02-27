from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    if len(letters) < 4:
        return set()
    c = Counter(letters)
    half = []
    middle = ''
    for letter, count in c.items():
        half.append(letter * (count // 2))
        if count % 2 and (not middle):
            middle = letter
    half = ''.join(half)
    palindromes = set()
    for p in set(permutations(half)):
        p = ''.join(p)
        palindromes.add(p + middle + p[::-1])
    palindromes = {p for p in palindromes if len(p) >= 4}
    return palindromes