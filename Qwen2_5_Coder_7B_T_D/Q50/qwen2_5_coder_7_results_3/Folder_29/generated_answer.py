from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_counter = Counter(sorted_word)
            for other_word in words:
                if other_word != word:
                    sorted_other_word = ''.join(sorted(other_word.lower()))
                    if sorted_other_word == sorted_word and Counter(sorted_other_word) == word_counter:
                        anagram_count += 1
    return anagram_count >= 35