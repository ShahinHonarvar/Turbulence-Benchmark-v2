import collections

def if_contains_anagrams(strings):
    anagram_counts = collections.Counter()
    for string in strings:
        canonical_string = ''.join(sorted(string.lower()))
        if len(canonical_string) >= 3:
            anagram_counts[canonical_string] += 1
    return max(anagram_counts.values()) <= 30