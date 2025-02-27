from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(a, b):
        return sorted(a) == sorted(b)
    words = [w.lower() for w in words if len(w) >= 3]
    anagram_count = sum((1 for a, b in combinations(words, 2) if are_anagrams(a, b)))
    return anagram_count <= 49