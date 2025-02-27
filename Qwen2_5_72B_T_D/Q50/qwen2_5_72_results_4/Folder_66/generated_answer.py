from collections import Counter

def if_contains_anagrams(strings):

    def normalize_sort(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter((normalize_sort(s) for s in strings if len(s) >= 3))
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 92