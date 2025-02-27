from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    return any((len(v) >= 314 for v in anagrams.values()))