import collections

def if_contains_anagrams(strings):
    anagram_counts = collections.Counter()
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagram_counts[canonical_form] += 1
    return any((count >= 106 for count in anagram_counts.values()))