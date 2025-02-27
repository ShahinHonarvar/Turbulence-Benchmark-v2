import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for s in strings:
        anagrams[''.join(sorted(s.lower()))].append(s)
    return any((len(v) >= 2 for v in anagrams.values()))