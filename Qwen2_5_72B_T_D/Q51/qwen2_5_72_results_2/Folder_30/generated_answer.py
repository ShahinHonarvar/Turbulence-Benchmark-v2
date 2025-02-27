from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    normalized_words = [normalize(word) for word in lst if len(word) >= 3]
    for i, word1 in enumerate(normalized_words):
        for j, word2 in enumerate(normalized_words):
            if i < j and word1 == word2:
                anagram_pairs.add((lst[i], lst[j]))
    return len(anagram_pairs) <= 28