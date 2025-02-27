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
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 10