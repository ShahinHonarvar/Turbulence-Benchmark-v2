from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(string1, string2):
        return sorted(string1.lower()) == sorted(string2.lower())
    valid_anagrams = [pair for pair in combinations(strings, 2) if 3 <= len(pair[0]) <= len(pair[1]) and is_anagram(*pair)]
    return len(valid_anagrams) <= 60