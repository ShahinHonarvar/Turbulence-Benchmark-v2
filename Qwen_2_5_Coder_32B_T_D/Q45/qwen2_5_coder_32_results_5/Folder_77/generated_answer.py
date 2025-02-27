from itertools import permutations
    import string

def palindromes_between_indices(s):
    chars = ''.join(filter(lambda x: x in string.ascii_letters, s[4:7])).lower()
    p = set()
    for i in range(2, len(chars) // 2 + 1):
        for perm in permutations(chars, i):
            half = ''.join(perm)
            p.add(half + half[::-1])
            if len(half) > 1:
                p.add(half + half[-2::-1])
    return {x for x in p if len(x) >= 4}