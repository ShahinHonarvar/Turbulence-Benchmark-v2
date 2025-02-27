from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and len(str2) >= 3 and (Counter(str1.lower()) == Counter(str2.lower()))
    anagram_pairs = [(s1, s2) for s1, s2 in combinations(strings, 2) if is_anagram(s1, s2)]
    return len(anagram_pairs) <= 66