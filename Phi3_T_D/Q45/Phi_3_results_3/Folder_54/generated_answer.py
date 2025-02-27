from itertools import permutations
from collections import Counter

def palindromes_between_indices(s):
    segment = s[4:10].lower()
    freq_dict = Counter(segment)
    odd_count = sum((n % 2 for n in freq_dict.values()))
    if odd_count > 1:
        return set()
    half = ''.join((k * (v // 2) for k, v in freq_dict.items()))
    half_perms = set(permutations(sorted(half)))
    palindromes = [''.join(left + middle + left[::-1]) for left in half_perms for mid in ('',) if len(left) > 1 or odd_count == 1]
    return set(palindromes)