import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:7])).lower()
    count = Counter(letters)
    mid = ''
    sides = []
    for char in count:
        if count[char] % 2:
            if not mid:
                mid = char
            else:
                continue
        sides.append(char * (count[char] // 2))
    palindromes = set()
    for perm in itertools.permutations(''.join(sides)):
        palindromes.add(''.join(perm) + mid + ''.join(reversed(perm)))
    return {p for p in palindromes if len(p) >= 3}