from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for item in lst:
        if len(item) >= 3:
            normalized = normalize(item)
            anagram_counts[normalized] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 416