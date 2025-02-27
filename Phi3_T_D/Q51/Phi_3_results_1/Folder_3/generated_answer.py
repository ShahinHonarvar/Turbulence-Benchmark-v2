from collections import Counter

def count_anagrams(word_list):
    anagram_count = 0
    checked = set()
    for word1 in word_list:
        for word2 in word_list:
            if word1 != word2 and sorted(word1.lower()) == sorted(word2.lower()) and (len(word1) >= 3):
                sorted_word = tuple(sorted(word1.lower()))
                if sorted_word not in checked:
                    anagram_count += word_list.count(word2)
                    checked.add(sorted_word)
    return anagram_count

def if_contains_anagrams(strings_list):
    return count_anagrams(strings_list) <= 66