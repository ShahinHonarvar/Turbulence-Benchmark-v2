from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            for item in d[sorted_s]:
                count += 1
                if count >= 153:
                    return True
            d[sorted_s].append(s)
    return False