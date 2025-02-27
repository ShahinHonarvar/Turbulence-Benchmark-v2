from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and len(sorted_s) >= 6:
            anagrams[sorted_s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_pairs >= 75