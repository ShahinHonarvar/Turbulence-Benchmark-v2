from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    words = [w.lower() for w in words if len(w) >= 3]
    pairs = combinations(words, 2)
    anagram_count = sum((1 for w1, w2 in pairs if is_anagram(w1, w2)))
    return anagram_count <= 392