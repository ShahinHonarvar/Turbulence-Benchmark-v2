from collections import Counter

def if_contains_anagrams(lst):

    def sorted_counter(s):
        return str(sorted(Counter(s.lower()).items()))
    count = 0
    seen_anagrams = set()
    for s in lst:
        if len(s) < 3:
            continue
        sc = sorted_counter(s)
        if sc in seen_anagrams:
            count += 1
        else:
            seen_anagrams.add(sc)
    return count >= 24