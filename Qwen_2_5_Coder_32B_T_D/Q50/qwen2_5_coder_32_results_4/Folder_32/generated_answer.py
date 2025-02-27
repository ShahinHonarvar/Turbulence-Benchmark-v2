from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3:
            anagram_counts[s] += 1
    total_anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return total_anagram_pairs >= 194