import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [s]
    return len(list(itertools.combinations(anagrams.values(), 2))) >= 92