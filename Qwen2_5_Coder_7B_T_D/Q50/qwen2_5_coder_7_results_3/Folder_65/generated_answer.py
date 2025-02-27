from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            count += len([x for x in defaultdict(list).values() if len(x) > 1 and [sorted_s] == x])
    return count >= 94