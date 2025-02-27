from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    count = Counter(letters)
    available = ''.join((c * (count[c] // 2) for c in count))
    palindromes = set()
    for perm in permutations(available):
        half = ''.join(perm)
        full = half + (''.join([c for c in count if count[c] % 2]) + half[::-1])
        if len(full) >= 5:
            palindromes.add(full)
    return palindromes