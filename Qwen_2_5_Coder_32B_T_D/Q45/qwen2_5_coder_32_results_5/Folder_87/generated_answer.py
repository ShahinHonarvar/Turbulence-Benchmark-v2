from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10])).lower()
    counter = Counter(letters)
    half = []
    middle = ''
    for char, cnt in counter.items():
        half.append(char * (cnt // 2))
        if cnt % 2 and (not middle):
            middle = char
    half = ''.join(half)
    palindromes = set()
    for perm in set(itertools.permutations(half)):
        palindromes.add(''.join(perm) + middle + ''.join(reversed(perm)))
    return {p for p in palindromes if len(p) >= 3}