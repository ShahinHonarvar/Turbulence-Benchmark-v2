from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_pairs = 0
    for word1, word2 in combinations(lst, 2):
        if Counter(word1) == Counter(word2):
            anagram_pairs += 1
    return anagram_pairs >= 153