import itertools

def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(s)
    num_anagrams = 0
    for group in anagram_groups.values():
        num_anagrams += len(list(itertools.combinations(group, 2)))
    return num_anagrams <= 17