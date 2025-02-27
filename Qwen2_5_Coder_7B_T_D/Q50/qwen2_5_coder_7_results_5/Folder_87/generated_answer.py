def if_contains_anagrams(lst):
    counts = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in counts:
                counts[sorted_s] += 1
            else:
                counts[sorted_s] = 1
    pairs = sum((v * (v - 1) // 2 for v in counts.values() if v >= 2))
    return pairs >= 88