def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in count:
                count[norm] += 1
            else:
                count[norm] = 1
    pairs = 0
    for val in count.values():
        if val > 1:
            pairs += val * (val - 1) // 2
    return pairs >= 69