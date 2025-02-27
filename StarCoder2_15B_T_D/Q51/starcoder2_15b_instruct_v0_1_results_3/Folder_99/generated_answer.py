import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = tuple(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 93