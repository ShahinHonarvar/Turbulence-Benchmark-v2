from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    word_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
    anagram_pairs = 0
    for key in word_map:
        if len(word_map[key]) > 1:
            anagram_pairs += len(word_map[key]) * (len(word_map[key]) - 1) // 2
    return anagram_pairs >= 189