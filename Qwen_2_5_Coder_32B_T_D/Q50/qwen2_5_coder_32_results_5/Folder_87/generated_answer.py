from itertools import combinations
    from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    seen = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in seen:
                seen[sorted_s] += 1
            else:
                seen[sorted_s] = 1
    for key in seen:
        if seen[key] > 1:
            count += combinations(seen[key], 2)
    return count >= 88