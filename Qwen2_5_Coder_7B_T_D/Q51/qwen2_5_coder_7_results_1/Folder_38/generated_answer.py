from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(word):
        return Counter(word.lower())
    word_count = [count_anagrams(word) for word in lst if len(word) >= 3]
    anagram_pairs = sum((word_count[i] == word_count[j] for i in range(len(word_count)) for j in range(i + 1, len(word_count))))
    return anagram_pairs <= 416