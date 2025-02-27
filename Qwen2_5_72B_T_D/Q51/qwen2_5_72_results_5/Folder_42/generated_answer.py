from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagrams = defaultdict(int)
    for s in strings:
        anagrams[''.join(sorted(s))] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 38