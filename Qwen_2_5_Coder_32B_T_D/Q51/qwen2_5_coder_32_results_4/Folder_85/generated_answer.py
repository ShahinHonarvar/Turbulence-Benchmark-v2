from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    seen_anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            seen_anagrams[sorted_s].append(s)
    for key in seen_anagrams:
        if len(seen_anagrams[key]) > 1:
            anagram_counts[key] = len(list(combinations(seen_anagrams[key], 2)))
    total_anagram_pairs = sum(anagram_counts.values())
    return total_anagram_pairs <= 276