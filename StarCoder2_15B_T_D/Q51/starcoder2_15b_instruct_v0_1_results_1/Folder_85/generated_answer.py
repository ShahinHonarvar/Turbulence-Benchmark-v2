import itertools

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_pairs = []
    for word1, word2 in itertools.combinations(words, 2):
        if is_anagram(word1, word2):
            anagram_pairs.append((word1, word2))
    return len(anagram_pairs) <= 276