import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        key = tuple(sorted(string.lower()))
        anagrams[key].append(string)
    return max(len(list(anagrams.values()))) <= 28