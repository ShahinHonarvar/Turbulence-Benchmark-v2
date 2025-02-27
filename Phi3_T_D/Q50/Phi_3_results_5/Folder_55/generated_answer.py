from collections import defaultdict
import itertools

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    count = 0
    for lst in anagrams.values():
        if len(lst[0]) >= 3:
            anagram_pairs = list(itertools.combinations(lst, 2))
            count += len(anagram_pairs)
    return count >= 15