from collections import defaultdict
import itertools

def if_contains_anagrams(strings):
    anagram_count = 0
    min_length = 3
    strings_sorted = [''.join(sorted(s.lower())) for s in strings if len(s) >= min_length]
    seen = set()
    for item in strings_sorted:
        if item in seen:
            anagram_count += 1
        else:
            seen.add(item)
    return anagram_count >= 94