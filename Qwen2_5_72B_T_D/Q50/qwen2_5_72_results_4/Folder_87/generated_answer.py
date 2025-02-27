def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in anagrams:
                anagrams[norm] += 1
            else:
                anagrams[norm] = 1
    count = sum((1 for v in anagrams.values() if v > 1))
    return count >= 88