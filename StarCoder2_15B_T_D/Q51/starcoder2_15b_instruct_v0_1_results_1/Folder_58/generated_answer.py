from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            anagram_counter[canonical_form] += 1
    return max(anagram_counter.values()) <= 60