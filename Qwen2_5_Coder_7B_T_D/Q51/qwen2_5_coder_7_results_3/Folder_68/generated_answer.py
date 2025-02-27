from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    words = [word.lower() for word in lst if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if Counter(words[i]) == Counter(words[j]):
                anagram_pairs += 1
            if anagram_pairs > 94:
                return False
    return True