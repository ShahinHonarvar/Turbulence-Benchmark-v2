from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = list(s)
    palindromes = set()
    for length in range(6, len(s) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm[:length // 2])
            full = half + half[::-1] if length % 2 == 0 else half + half[-2::-1]
            if full in palindromes:
                continue
            if full == full[::-1]:
                palindromes.add(full)
    return palindromes