from itertools import combinations

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and sorted_word(word1) == sorted_word(word2):
            anagram_count += 1
    return anagram_count >= 79