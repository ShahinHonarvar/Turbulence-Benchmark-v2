from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    words = [w.lower() for w in words if len(w) >= 3]
    anagram_count = sum((1 for a, b in combinations(words, 2) if Counter(a) == Counter(b)))
    return anagram_count <= 423