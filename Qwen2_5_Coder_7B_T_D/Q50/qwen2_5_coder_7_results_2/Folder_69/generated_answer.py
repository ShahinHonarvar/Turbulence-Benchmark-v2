from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        anagrams[sorted_s].append(s_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return anagram_pairs >= 188