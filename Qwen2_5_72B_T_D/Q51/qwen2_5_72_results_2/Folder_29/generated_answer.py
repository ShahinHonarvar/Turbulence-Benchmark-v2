from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_pairs = 0
    for str1, str2 in combinations(lst, 2):
        if is_anagram(str1, str2):
            anagram_pairs += 1
    return anagram_pairs <= 318