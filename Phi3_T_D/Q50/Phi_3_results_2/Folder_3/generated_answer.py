from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(strings):
    sorted_strings = [(''.join(sorted(s.lower())), len(s)) for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(int)
    for _, length in sorted_strings:
        anagram_dict[length] += 1
    count = 0
    for length, frequency in anagram_dict.items():
        if frequency > 1:
            perms = set((''.join(p) for p in permutations('abcdefghijklmnopqrstuvwxyz', length)))
            found_chars = set()
            unique_perms = set()
            for _, sorted_str in sorted_strings:
                if sorted_str in perms and sorted_str not in found_chars:
                    found_chars.add(sorted_str)
                    unique_perms.add(sorted_str)
                    if len(unique_perms) == frequency:
                        count += frequency
                    if count >= 30:
                        return True
    return False