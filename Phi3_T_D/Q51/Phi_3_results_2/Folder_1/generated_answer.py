from collections import defaultdict

def if_contains_anagrams(string_list):

    def char_count(s):
        s = s.lower()
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        return frozenset(counts.items())
    anagram_counts = defaultdict(int)
    for s in string_list:
        if len(s) >= 3:
            anagram_counts[char_count(s)] += 1
    anagram_pairs = sum((val * (val - 1) // 2 for val in anagram_counts.values()))
    return anagram_pairs <= 30