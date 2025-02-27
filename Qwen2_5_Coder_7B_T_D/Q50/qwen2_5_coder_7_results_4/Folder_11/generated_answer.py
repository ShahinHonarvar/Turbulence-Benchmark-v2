from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            counter = Counter([sorted_s])
            count += counter[sorted_s] - 1
    return count >= 28