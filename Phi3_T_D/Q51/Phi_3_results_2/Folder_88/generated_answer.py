def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = {}
    for s in lst:
        if len(s) >= 3:
            norm = normalize(s)
            counts[norm] = counts.get(norm, 0) + 1
    return sum((c * (c - 1) // 2 for c in counts.values())) <= 407