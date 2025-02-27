from itertools import combinations

def if_contains_anagrams(words):

    def sorted_letters(word):
        return tuple(sorted(word.lower()))
    anagram_count = 0
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            key = sorted_letters(word)
            word_dict[key] = word_dict.get(key, 0) + 1
    for count in word_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 91