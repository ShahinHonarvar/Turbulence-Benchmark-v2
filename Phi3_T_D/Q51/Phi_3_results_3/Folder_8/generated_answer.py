from itertools import combinations

def if_contains_anagrams(strings):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_pairs = [(s1, s2) for i, s1 in enumerate(strings) for s2 in strings[i + 1:] if are_anagrams(s1, s2) and len(s1) >= 3 and (len(s2) >= 3)]
    return len(anagram_pairs) <= 68