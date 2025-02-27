from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s)).lower()
        if len(s) >= 3:
            anagrams[sorted_s] += 1
    return sum((count > 1 for count in anagrams.values())) >= 35