from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    word_count = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            if word_count[normalized_word] > 0:
                anagram_pairs.add((word, word_count[normalized_word]))
            word_count[normalized_word] += 1
    return len(anagram_pairs) <= 42