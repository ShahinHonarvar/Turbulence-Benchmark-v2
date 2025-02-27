from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        canonical_form = ''.join(sorted(s.lower()))
        anagram_counts[canonical_form] += 1
    return any((count >= 86 for count in anagram_counts.values()))