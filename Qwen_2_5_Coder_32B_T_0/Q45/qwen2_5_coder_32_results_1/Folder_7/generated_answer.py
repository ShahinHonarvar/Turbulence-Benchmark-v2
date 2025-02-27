from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:10])).lower()
    count = Counter(letters)
    mid, sides = ('', [])
    for char, freq in count.items():
        if freq % 2:
            mid = char
            freq -= 1
        sides.extend(char * (freq // 2))
    if len(mid) + 2 * len(sides) < 7:
        return set()
    palindromes = set()
    for side in set(permutations(sides)):
        palindromes.add(''.join(side) + mid + ''.join(reversed(side)))
    return palindromes