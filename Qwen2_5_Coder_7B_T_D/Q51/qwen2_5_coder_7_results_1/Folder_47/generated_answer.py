from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    anagram_pairs = []
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            anagram_pairs.append((str1, str2))
    return len(anagram_pairs) <= 366