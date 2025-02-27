def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in counts:
                counts[norm] += 1
            else:
                counts[norm] = 1
    return sum((v * (v - 1) // 2 for v in counts.values())) >= 194