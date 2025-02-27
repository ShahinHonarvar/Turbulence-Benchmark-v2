from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_counts[sort_string(s)] += 1
    return sum((c * (c - 1) // 2 for c in anagram_counts.values())) <= 257