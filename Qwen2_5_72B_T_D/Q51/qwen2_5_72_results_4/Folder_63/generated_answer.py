from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            anagram_counts[s_sorted] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 423