def if_contains_anagrams(input_list):
    anagrams = {}
    for s in input_list:
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return any((len(v) >= 11 for v in anagrams.values()))