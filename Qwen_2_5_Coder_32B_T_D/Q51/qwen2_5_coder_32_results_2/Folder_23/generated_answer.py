from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_count = 0
    for word1, word2 in combinations(words, 2):
        if Counter(word1) == Counter(word2):
            anagram_count += 1
            if anagram_count > 49:
                return False
    return True