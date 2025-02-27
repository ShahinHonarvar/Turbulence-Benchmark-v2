import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = tuple(sorted(s.lower()))
        anagrams[key] = anagrams.get(key, []) + [s]
    return len(list(filter(lambda x: len(x) >= 88, anagrams.values()))) > 0