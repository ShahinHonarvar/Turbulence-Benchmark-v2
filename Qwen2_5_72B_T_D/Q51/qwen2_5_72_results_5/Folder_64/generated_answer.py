from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_counter = 0
    for i, word1 in enumerate(lst):
        for word2 in lst[i + 1:]:
            if Counter(word1) == Counter(word2):
                anagram_counter += 1
                if anagram_counter > 59:
                    return False
    return True