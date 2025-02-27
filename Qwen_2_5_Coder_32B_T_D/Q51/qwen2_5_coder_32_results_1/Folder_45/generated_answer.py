from collections import Counter

def if_contains_anagrams(lst):

    def sorted_counts(s):
        return frozenset(Counter(s.lower()).items())
    count_map = Counter((sorted_counts(s) for s in lst if len(s) >= 3))
    return sum((v * (v - 1) // 2 for v in count_map.values())) <= 464