from itertools import combinations

def if_contains_anagrams(words):
    words = [''.join(sorted(w.lower())) for w in words if len(w) >= 3]
    anagram_pairs = sum((1 for a, b in combinations(words, 2) if a == b))
    return anagram_pairs <= 24