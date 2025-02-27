from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_count = sum((1 for w1, w2 in combinations(words, 2) if are_anagrams(w1, w2)))
    return anagram_count <= 22