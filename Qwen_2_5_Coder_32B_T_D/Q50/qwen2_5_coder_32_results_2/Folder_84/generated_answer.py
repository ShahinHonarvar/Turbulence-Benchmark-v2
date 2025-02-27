from collections import defaultdict

def if_contains_anagrams(strings):
    a = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            a[sorted_s].append(s_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in a.values()))
    return anagram_pairs >= 108