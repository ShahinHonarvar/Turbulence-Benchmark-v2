from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count = Counter([sorted_word])
            anagram_pairs += count[sorted_word] - 1
    return anagram_pairs >= 18