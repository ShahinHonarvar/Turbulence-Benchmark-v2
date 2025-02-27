from collections import defaultdict
import itertools

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = 0
    for pairs in anagrams.values():
        anagram_pairs += sum((1 for _ in itertools.combinations(pairs, 2)))
        if anagram_pairs > 22:
            return False
    return True