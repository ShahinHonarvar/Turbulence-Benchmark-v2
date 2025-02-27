from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    count = Counter(letters)
    singles = [char for char, cnt in count.items() if cnt % 2 != 0]
    doubles = ''.join((char * (cnt // 2) for char, cnt in count.items()))
    palindromes = set()
    if len(singles) <= 1:
        for half in set(permutations(doubles)):
            half = ''.join(half)
            for single in singles:
                palindromes.add(half + single + half[::-1])
            if not singles:
                palindromes.add(half + half[::-1])
    result = {p for p in palindromes if len(p) >= 4}
    return result