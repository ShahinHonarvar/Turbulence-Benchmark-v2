from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10])).lower()
    count = Counter(letters)
    mid = []
    sides = []
    for char, cnt in count.items():
        mid.append(char)
        sides.extend(char * (cnt // 2))
    mid = [char for char in mid if count[char] % 2 != 0]
    palindromes = set()
    for m in permutations(mid):
        for s in set(permutations(sides)):
            pal = ''.join(s) + ''.join(m) + ''.join(s)[::-1]
            if len(pal) >= 7:
                palindromes.add(pal)
    return palindromes