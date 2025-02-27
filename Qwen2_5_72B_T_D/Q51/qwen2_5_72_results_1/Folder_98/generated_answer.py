def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in anagrams:
                anagrams[norm].append(s)
            else:
                anagrams[norm] = [s]
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 46