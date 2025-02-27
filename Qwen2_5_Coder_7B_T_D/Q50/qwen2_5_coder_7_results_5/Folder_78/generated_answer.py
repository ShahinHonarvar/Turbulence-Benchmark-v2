from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if Counter(sorted_s) == Counter(s.lower()):
                count += 1
    return count >= 79