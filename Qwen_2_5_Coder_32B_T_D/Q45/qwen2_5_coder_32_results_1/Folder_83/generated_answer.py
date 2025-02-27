from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    count = Counter(letters)
    half = []
    middle = ''
    for char, cnt in count.items():
        half.extend(char * (cnt // 2))
        if cnt % 2 and (not middle):
            middle = char
    half_perms = set((''.join(p) for p in itertools.permutations(half)))
    return {h + middle + h[::-1] for h in half_perms if len(h) * 2 + len(middle) >= 7}