from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_sets = defaultdict(set)
    counter = 0
    for s in strings:
        key = ''.join(sorted(s.lower()))
        anagram_sets[key].add(s)
    for _, group in anagram_sets.items():
        if len(group) >= 2:
            counter += len(group) * (len(group) - 1) // 2
    return counter >= 73