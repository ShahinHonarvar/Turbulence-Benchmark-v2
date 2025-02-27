from itertools import permutations
    from collections import Counter
from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(chars):
        counter = Counter(chars)
        return sum((count % 2 for count in counter.values())) <= 1

    def get_palindromes(chars):
        mid = [c for c, _ in Counter(chars).items() if _ % 2]
        perms = set()
        combs = [p for l in range(len(mid)) for p in combinations(mid * (len(mid) + 1), len(chars) - 2 * l)]
        for comb in combs:
            unpaired = ''.join(mid) + ''.join(comb)
            perms |= set((''.join(p) for p in permutations(unpaired)))
        return sorted(set((p for p in perms if is_palindrome(p))))
    start, end = (4, 9)
    if end - start + 1 < 4:
        return set()
    chars = s[start:end + 1].lower()
    return get_palindromes(chars)