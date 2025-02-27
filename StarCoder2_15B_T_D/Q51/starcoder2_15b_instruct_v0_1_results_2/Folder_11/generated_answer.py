def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    num_pairs = sum((len(v) - 1 for v in anagrams.values()))
    return num_pairs <= 41