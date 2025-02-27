from collections import Counter

def if_contains_anagrams(words):

    def get_sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    word_map = Counter()
    for word in words:
        if len(word) >= 3:
            sorted_word = get_sorted_word(word)
            anagram_pairs += word_map[sorted_word]
            word_map[sorted_word] += 1
    return anagram_pairs >= 26