import collections

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            count += sum((1 for v in collections.Counter(sorted_s).values() if v > 1))
    return count // 2 <= 49