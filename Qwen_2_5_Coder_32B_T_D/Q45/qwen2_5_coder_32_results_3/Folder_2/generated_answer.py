import itertools
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:6])).lower()
    count = Counter(letters)
    mid = ''
    sides = []
    for char, cnt in count.items():
        mid += char * (cnt % 2)
        sides.append(char * (cnt // 2))
    if len(mid) > 1:
        return set()
    mid = mid[0] if mid else ''
    palindromes = set()
    for p in itertools.permutations(''.join(sides)):
        p_str = ''.join(p)
        palindromes.add(p_str + mid + p_str[::-1])
    return palindromes