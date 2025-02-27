from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_counter = 0
    for i, word1 in enumerate(strings):
        sorted_word1 = ''.join(sorted(word1))
        for word2 in strings[i + 1:]:
            sorted_word2 = ''.join(sorted(word2))
            if sorted_word1 == sorted_word2:
                anagram_counter += 1
    return anagram_counter <= 131