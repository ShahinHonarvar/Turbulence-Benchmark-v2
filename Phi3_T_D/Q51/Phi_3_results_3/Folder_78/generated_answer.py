from collections import defaultdict
import itertools

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        anagrams[key].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1 and len(key) >= 3:
            combinations = itertools.combinations(anagrams[key], 2)
            count += sum((1 for _ in combinations))
    return count <= 70