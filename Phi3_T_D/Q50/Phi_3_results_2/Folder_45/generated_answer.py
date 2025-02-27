from collections import defaultdict

def if_contains_anagrams(strings):

    def count_chars(s):
        return sorted(s.lower())
    sorted_strings = [(count_chars(s), s) for s in strings if len(s) >= 3]
    anagram_counts = defaultdict(int)
    for key, _ in sorted_strings:
        anagram_counts[key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 277