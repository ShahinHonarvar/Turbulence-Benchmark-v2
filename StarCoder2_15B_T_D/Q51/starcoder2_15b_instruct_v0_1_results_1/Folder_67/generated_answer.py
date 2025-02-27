import collections

def if_contains_anagrams(strings):
    anagram_counter = collections.Counter()
    for string in strings:
        canonical_string = ''.join(sorted(string.lower()))
        anagram_counter[canonical_string] += 1
    return max(anagram_counter.values()) <= 5