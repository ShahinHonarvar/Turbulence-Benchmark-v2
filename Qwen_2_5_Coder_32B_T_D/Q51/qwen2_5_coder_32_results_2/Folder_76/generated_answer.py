from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def sorted_tuple(s):
        return tuple(sorted(s.lower()))
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            count[sorted_tuple(word)] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs <= 91