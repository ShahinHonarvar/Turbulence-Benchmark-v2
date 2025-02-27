from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = [pair for pair in combinations(strings, 2) if is_anagram(*pair)]
    return len(anagram_pairs) >= 35