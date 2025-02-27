def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    potential_anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in potential_anagrams:
            potential_anagrams[norm].append(s)
        else:
            potential_anagrams[norm] = [s]
    count = sum((len(v) // 2 for v in potential_anagrams.values() if len(v) >= 2))
    return count >= 43