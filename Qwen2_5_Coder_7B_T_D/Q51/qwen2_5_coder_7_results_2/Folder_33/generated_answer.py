from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_pairs <= 85