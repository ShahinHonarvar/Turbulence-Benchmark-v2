def if_contains_anagrams(strings):
    if len(strings) < 140:
        return False
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    for v in anagrams.values():
        if len(v) >= 3:
            return True
    return False