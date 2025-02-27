from math import comb
    from collections import defaultdict
import math

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))

    def poten_permut(n):
        return min((26 ** i * math.comb(n, i) for i in range(3, n + 1)))
    str_groups = defaultdict(list)
    for string in strings:
        norm_str = normalize_string(string)
        str_groups[norm_str].append(string)
    anagram_pairs = 0
    for group in str_groups.values():
        while len(group) > 1:
            pair = group.pop()
            for other in group:
                if ''.join(sorted(pair.lower())) == ''.join(sorted(other.lower())):
                    anagram_pairs += 1
                    break
    return anagram_pairs <= 276