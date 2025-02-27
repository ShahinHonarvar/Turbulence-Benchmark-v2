import collections
import itertools

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    return len(list(itertools.combinations(anagrams.values(), 2))) <= 131