from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    sorted_by_length = sorted((string for string in strings if len(string) >= 3))
    anagrams_map = defaultdict(list)
    for string in sorted_by_length:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams_map[sorted_string].append(string)
    anagram_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagrams_map.values() if len(anagrams) > 1))
    return anagram_count >= 153