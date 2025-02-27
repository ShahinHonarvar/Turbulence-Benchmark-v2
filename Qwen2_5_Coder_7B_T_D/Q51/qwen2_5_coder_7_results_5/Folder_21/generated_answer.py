from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagrams = set()
    for word1, word2 in combinations(lst, 2):
        if len(word1) >= 3 == len(word2) >= 3 and Counter(word1.lower()) == Counter(word2.lower()):
            anagrams.add(tuple(sorted([word1, word2])))
    return len(anagrams) <= 26