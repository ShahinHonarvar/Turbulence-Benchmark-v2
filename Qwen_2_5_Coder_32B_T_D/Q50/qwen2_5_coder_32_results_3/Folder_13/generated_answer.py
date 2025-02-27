from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    seen = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in seen:
                seen[sorted_s] += 1
            else:
                seen[sorted_s] = 1
            count += seen[sorted_s] - 1
            if count >= 144:
                return True
    return False