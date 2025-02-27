from itertools import combinations

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_pairs = [pair for pair in combinations(strings, 2) if len(pair[0]) >= 3 and len(pair[1]) >= 3 and are_anagrams(*pair)]
    return len(valid_pairs) <= 173