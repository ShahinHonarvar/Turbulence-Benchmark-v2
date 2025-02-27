import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = tuple(sorted(s.lower()))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 36