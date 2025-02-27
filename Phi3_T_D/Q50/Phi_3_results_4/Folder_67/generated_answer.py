from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_counts[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values() if count >= 2))
    return anagram_pairs >= 41