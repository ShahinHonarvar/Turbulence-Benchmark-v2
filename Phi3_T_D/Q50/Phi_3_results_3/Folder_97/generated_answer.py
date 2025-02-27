from itertools import combinations

def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    anagram_count = sum((sorted_words.count(anagram) > 1 for anagram in set(sorted_words)))
    return anagram_count >= 123