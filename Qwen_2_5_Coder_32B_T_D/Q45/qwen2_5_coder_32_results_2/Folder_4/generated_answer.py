from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    s = s[3:10].lower()
    letters = ''.join([c for c in s if c in string.ascii_lowercase])
    count = Counter(letters)
    mid = ''
    sides = []
    for c in count:
        if count[c] % 2 == 1:
            if mid:
                break
            mid = c
        sides.append(c * (count[c] // 2))
    sides = ''.join(sides)
    perms = set([''.join(p) for p in permutations(sides)])
    palindromes = {side + mid + side[::-1] for side in perms if len(side) * 2 + len(mid) >= 7}
    return palindromes