from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    count = Counter(letters)
    mid = ''
    sides = []
    for char, freq in count.items():
        if freq % 2:
            if mid:
                break
            mid = char
        sides.extend(char * (freq // 2))
    else:
        perms = set(permutations(sides))
        return {''.join(side) + mid + ''.join(side[::-1]) for side in perms if len(side) * 2 + len(mid) >= 7}
    return set()