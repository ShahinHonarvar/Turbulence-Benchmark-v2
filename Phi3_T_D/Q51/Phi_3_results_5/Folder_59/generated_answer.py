from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = [(s1, s2) for s1, s2 in combinations(strings, 2) if is_anagram(s1, s2) and len(s1) >= 3 and (len(s2) >= 3)]
    return len(anagram_pairs) <= 15