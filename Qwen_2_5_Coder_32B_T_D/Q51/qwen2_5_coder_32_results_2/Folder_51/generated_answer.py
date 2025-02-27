from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):

    def are_anagrams(word1, word2):
        return Counter(word1) == Counter(word2)
    words = [''.join(filter(str.isalpha, w.lower())) for w in words]
    words = [w for w in words if len(w) >= 3]
    pairs = combinations(words, 2)
    anagram_count = sum((1 for w1, w2 in pairs if are_anagrams(w1, w2)))
    return anagram_count <= 116