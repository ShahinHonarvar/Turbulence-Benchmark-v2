from collections import defaultdict

def if_contains_anagrams(word_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def filter_valid_anagrams(word_list):
        valid_anagrams = []
        for i, word1 in enumerate(word_list):
            for word2 in word_list[i + 1:]:
                if is_anagram(word1, word2) and len(word1) >= 3 and (len(word2) >= 3):
                    valid_anagrams.append((word1, word2))
        return valid_anagrams
    anagram_pairs = filter_valid_anagrams(word_list)
    return len(anagram_pairs) <= 25