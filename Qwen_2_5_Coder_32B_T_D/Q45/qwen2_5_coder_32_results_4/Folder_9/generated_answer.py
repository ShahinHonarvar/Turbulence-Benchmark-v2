from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    count = Counter(letters)
    mid = ''
    sides = []
    for char, cnt in count.items():
        if cnt % 2:
            if mid:
                return set()
            mid = char
        sides.extend(char * (cnt // 2))
    palindromes = set()
    for side in set(permutations(sides)):
        palindromes.add(''.join(side) + mid + ''.join(reversed(side)))
    return palindromes