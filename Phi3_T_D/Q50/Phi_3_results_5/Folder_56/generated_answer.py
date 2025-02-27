def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            counts[norm] = counts.get(norm, 0) + 1
    return sum((v * (v - 1) // 2 for v in counts.values())) >= 77