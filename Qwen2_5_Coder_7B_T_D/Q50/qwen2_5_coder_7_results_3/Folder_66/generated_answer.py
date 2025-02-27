from collections import Counter

def if_contains_anagrams(words):

    def sorted_chars(word):
        return sorted(word.lower())
    word_map = Counter((sorted_chars(word) for word in words if len(word) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_map.values()))
    return anagram_pairs >= 92