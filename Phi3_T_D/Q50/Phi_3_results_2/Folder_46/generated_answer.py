from collections import defaultdict

def if_contains_anagrams(strings):

    def to_sorted_tuple(s):
        return tuple(sorted(s.lower()))
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            counts[to_sorted_tuple(s)] += 1
    return sum((count > 1 for count in counts.values())) >= 38