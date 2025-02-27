from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = Counter()
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagram_counts[canonical_form] += 1
    return max(anagram_counts.values()) <= 255