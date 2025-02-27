from collections import defaultdict

def if_contains_anagrams(strings):
    length_filtered = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = defaultdict(int)
    for string in length_filtered:
        anagram_counts[string] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 38