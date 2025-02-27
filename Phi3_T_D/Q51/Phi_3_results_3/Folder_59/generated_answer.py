from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = defaultdict(int)
    for s in sorted_strings:
        counter[s] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 15