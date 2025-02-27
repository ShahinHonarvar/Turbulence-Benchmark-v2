import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = tuple(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 464