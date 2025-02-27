from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    for word1 in words:
        for word2 in words:
            if word1 != word2 and len(word1) >= 3 and (len(word2) >= 3):
                if Counter(word1.lower()) == Counter(word2.lower()):
                    anagram_count += 1
    return anagram_count >= 47