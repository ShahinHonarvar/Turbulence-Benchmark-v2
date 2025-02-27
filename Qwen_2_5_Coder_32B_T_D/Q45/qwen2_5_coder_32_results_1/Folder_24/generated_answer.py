from itertools import permutations, combinations
    from collections import Counter

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    n = len(letters)
    palindromes = set()
    for r in range(4, n + 1):
        for comb in combinations(letters, r):
            count = Counter(comb)
            half = ''.join((c * (count[c] // 2) for c in count))
            if len(half) * 2 == r or (len(half) * 2 + 1 == r and count.most_common(1)[0][1] > len(half)):
                for perm in set(permutations(half)):
                    p = ''.join(perm) + (count.most_common(1)[0][0] if len(half) * 2 + 1 == r else '') + ''.join(reversed(perm))
                    palindromes.add(p)
    return palindromes