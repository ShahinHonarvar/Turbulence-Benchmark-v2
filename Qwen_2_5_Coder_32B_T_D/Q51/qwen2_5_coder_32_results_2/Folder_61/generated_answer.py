from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    seen_anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            for anagram in seen_anagrams[sorted_s]:
                anagram_counts[s_lower, anagram] += 1
            seen_anagrams[sorted_s].append(s_lower)
    return sum(anagram_counts.values()) <= 50