from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    c = Counter(letters)
    doubles = ''.join((k * (v // 2) for k, v in c.items()))
    palindromes = set()
    for p in set(permutations(doubles)):
        mid = ''.join((k for k, v in c.items() if v % 2 != 0))
        palindromes.add(''.join(p) + mid + ''.join(p)[::-1])
    return {p for p in palindromes if len(p) >= 6}