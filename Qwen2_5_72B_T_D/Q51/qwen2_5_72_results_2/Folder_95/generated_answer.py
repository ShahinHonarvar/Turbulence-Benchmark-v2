from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_counts = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_counts[sorted_s] += 1
    anagram_pairs = sum((count - 1 for count in anagram_counts.values()))
    return anagram_pairs <= 6