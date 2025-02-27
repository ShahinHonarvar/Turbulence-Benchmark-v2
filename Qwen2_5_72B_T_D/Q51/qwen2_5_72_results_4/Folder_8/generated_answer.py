from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_pairs = 0
    for word1, word2 in combinations(strings, 2):
        if is_anagram(word1, word2):
            anagram_pairs += 1
    return anagram_pairs <= 68