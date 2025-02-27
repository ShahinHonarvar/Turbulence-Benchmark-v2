from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    anagram_pairs = 0
    for str1, str2 in combinations(words, 2):
        if is_anagram(str1, str2) and len(str1) >= 3:
            anagram_pairs += 1
        if anagram_pairs > 36:
            return False
    return anagram_pairs <= 36