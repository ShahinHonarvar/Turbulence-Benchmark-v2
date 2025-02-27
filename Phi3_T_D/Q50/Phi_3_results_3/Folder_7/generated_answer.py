from collections import defaultdict

def if_contains_anagrams(word_list):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagrams_count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if is_anagram(word_list[i], word_list[j]) and len(word_list[i]) >= 3 and (len(word_list[j]) >= 3):
                anagrams_count += 1
    return anagrams_count >= 178