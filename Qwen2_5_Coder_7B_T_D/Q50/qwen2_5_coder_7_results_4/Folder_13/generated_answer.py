from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(words):
        anagram_count = 0
        word_map = {}
        for word in words:
            sorted_word = ''.join(sorted(word.lower()))
            if len(sorted_word) >= 3:
                if sorted_word in word_map:
                    word_map[sorted_word] += 1
                    if word_map[sorted_word] == 2:
                        anagram_count += 1
                else:
                    word_map[sorted_word] = 1
        return anagram_count
    return count_anagrams(lst) >= 144