from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            anagram_dict[sorted_string(s)].append(s)
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1])
    return anagram_pairs >= 209