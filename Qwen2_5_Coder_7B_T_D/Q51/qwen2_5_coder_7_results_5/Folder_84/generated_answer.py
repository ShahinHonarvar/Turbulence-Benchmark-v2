from collections import Counter

def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagrams:
                return False
            anagrams.add(sorted_s)
    return True