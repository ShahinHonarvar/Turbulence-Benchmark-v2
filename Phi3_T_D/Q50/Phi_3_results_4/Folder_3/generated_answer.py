from itertools import combinations

def count_anagrams(word_list):
    anagram_count = 0
    for word1, word2 in combinations(word_list, 2):
        if sorted(word1.lower()) == sorted(word2.lower()):
            anagram_count += 1
    return anagram_count

def if_contains_anagrams(words):
    three_letter_words = [word.lower() for word in words if len(word) >= 3]
    return count_anagrams(three_letter_words) >= 30