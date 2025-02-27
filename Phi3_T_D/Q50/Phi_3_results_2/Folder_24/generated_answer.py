from collections import Counter

def if_contains_anagrams(strings):
    length_three_forward = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = Counter(length_three_forward)
    return sum((count >= 2 for count in anagram_counts.values())) >= 65