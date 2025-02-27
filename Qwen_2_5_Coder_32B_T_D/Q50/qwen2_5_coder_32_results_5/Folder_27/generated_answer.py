from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            count[sorted_s].append(s_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in count.values() if len(v) > 1))
    return anagram_pairs >= 86