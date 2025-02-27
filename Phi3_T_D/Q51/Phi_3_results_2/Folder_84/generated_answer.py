from collections import Counter

def if_contains_anagrams(strings):

    def count_letters(s):
        return Counter(filter(str.isalpha, s.lower()))
    distinct_words_counter = Counter([count_letters(word) for word in strings if len(word) >= 3])
    anagram_pairs = sum((val * (val - 1) // 2 for val in distinct_words_counter.values()))
    return anagram_pairs <= 16