from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    seen = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            seen[sorted_s].append(s)
            if len(seen[sorted_s]) == 2:
                count += 1
            elif len(seen[sorted_s]) > 2:
                count += len(seen[sorted_s]) - 1
    return count >= 123