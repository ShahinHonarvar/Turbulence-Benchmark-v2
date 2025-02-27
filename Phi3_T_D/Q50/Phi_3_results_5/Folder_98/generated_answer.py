from collections import defaultdict
import itertools

def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    string_groups = defaultdict(list)
    for s in strings_list:
        if len(s) >= 3:
            string_groups[normalize(s)].append(s)
    anagram_pairs = []
    for group in string_groups.values():
        for pair in itertools.combinations(group, 2):
            anagram_pairs.append(pair)
    return len(anagram_pairs) >= 7