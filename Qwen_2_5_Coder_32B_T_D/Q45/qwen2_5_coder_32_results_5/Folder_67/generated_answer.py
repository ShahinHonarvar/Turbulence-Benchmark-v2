from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.lower() in string.ascii_lowercase]
    count = Counter(letters)
    if len(letters) < 5:
        return set()
    mid, sides = ('', [])
    for char, cnt in count.items():
        if cnt % 2:
            mid = char
            cnt -= 1
        if cnt:
            sides.extend(char * (cnt // 2))
    if mid and len(sides) < 2:
        return set()
    elif not mid and (not sides):
        return set()
    elif not mid and len(sides) < 2.5:
        return set()
    palindromes = set()
    for perm in set(permutations(sides)):
        palindromes.add(''.join(perm) + mid + ''.join(reversed(perm)))
    return palindromes