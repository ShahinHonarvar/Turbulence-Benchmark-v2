from itertools import combinations
    from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for comb in combinations(strings, 2):
        if len(normalize(comb[0])) == len(normalize(comb[1])) >= 3:
            if normalize(comb[0]) == normalize(comb[1]):
                anagrams[comb] += 1
    return sum(anagrams.values()) <= 57