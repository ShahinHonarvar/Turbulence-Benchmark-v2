import collections
import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join((c for c in string.lower() if c.isalpha()))
        if len(string) >= 3:
            key = tuple(sorted(string))
            anagrams[key] = anagrams.get(key, []) + [string]
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 39