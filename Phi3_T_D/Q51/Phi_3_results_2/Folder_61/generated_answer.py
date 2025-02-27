from collections import Counter
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams_count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    seen_hashes = set()
    for string in sorted_strings:
        for other in seen_hashes:
            if Counter(string) == Counter(other):
                anagrams_count += 1
                if anagrams_count == 50:
                    return False
        seen_hashes.add(string)
    return True