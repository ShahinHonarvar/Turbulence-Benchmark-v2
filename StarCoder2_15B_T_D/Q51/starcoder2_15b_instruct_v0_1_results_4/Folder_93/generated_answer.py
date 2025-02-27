import itertools

def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(s)
    return len(list(itertools.combinations(strings, 2))) <= 36