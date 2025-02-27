from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams_count = 0
    strings_dict = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        strings_dict[sorted_string] += 1
    for count in strings_dict.values():
        if count > 1:
            anagrams_count += count * (count - 1) // 2
    return anagrams_count >= 42