from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:9].lower()
    letters = [char for char in s if char.isalpha()]
    count = Counter(letters)
    mid, half = ('', [])
    chars = set(letters)
    for char in chars:
        if count[char] % 2:
            mid += char
        half += char * (count[char] // 2)
    if len(mid) > 1:
        return set()
    palindromes = set()
    for perm in permutations(half):
        palindromes.add(''.join(perm) + mid + ''.join(reversed(perm)))
    return {p for p in palindromes if len(p) >= 3}