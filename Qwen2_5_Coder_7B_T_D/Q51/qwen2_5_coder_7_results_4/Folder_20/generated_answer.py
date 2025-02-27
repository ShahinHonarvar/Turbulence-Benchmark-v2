from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            anagram_count += lst.count(sorted_word) - 1
    return anagram_count <= 131