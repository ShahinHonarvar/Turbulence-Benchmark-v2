from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_counter = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            anagram_pairs += anagram_counter[normalized_word]
            anagram_counter[normalized_word] += 1
    return anagram_pairs <= 16