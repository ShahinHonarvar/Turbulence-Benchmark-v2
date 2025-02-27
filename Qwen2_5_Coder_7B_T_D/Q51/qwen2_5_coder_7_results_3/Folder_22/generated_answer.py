from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for word1 in lst:
        for word2 in lst[lst.index(word1) + 1:]:
            if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()) and (Counter(word1.lower()) == Counter(word2.lower())):
                anagram_count += 1
    return anagram_count <= 14