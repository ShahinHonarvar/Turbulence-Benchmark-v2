from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagram_counts[normalized] += 1
    pair_count = 0
    for count in anagram_counts.values():
        pair_count += count * (count - 1) // 2
    return pair_count >= 61