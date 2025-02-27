from collections import Counter

def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams.add(sorted_word)
    anagram_pairs = len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs <= 445