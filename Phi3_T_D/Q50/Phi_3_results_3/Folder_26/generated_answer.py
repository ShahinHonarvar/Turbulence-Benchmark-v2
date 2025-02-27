from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagrams[key].append(string)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 49