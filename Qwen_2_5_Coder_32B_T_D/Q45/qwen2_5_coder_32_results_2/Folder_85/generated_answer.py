from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.lower() in string.ascii_lowercase]
    count = Counter(letters)
    mid = ''
    sides = []
    for char, cnt in count.items():
        if cnt % 2 == 1 and (not mid):
            mid = char
        sides.extend(char * (cnt // 2))
    half_palindromes = set((''.join(p) for p in permutations(sides)))
    palindromes = {side + mid + side[::-1] for side in half_palindromes if len(side) * 2 + len(mid) >= 7}
    return palindromes