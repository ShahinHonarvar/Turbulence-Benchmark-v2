def if_contains_anagrams(lst):
    d = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in d:
            d[sorted_s] += 1
        else:
            d[sorted_s] = 1
    count = 0
    for k, v in d.items():
        count += v * (v - 1) // 2
    return count <= 257