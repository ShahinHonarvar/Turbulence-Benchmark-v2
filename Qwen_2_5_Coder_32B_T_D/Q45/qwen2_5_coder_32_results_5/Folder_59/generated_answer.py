from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[8:10].lower()))
    count = Counter(letters)
    mid = []
    even_sides = []
    for char, cnt in count.items():
        if cnt % 2:
            mid.append(char)
        even_sides.extend(char * (cnt // 2))
    palindromes = set()
    if len(mid) <= 1:
        for perm in set(itertools.permutations(even_sides)):
            half = ''.join(perm)
            full = half + (mid[0] if mid else '') + half[::-1]
            if len(full) >= 3:
                palindromes.add(full)
    return palindromes