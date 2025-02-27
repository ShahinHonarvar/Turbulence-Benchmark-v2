from itertools import combinations

def if_contains_anagrams(words):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    valid_pairs = [comb for comb in combinations(words, 2) if len(comb[0]) >= 3 and are_anagrams(*comb)]
    return len(valid_pairs) <= 60