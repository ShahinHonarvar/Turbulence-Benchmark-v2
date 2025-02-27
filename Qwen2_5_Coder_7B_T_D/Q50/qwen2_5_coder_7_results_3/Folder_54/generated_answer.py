from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    anagram_pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 74