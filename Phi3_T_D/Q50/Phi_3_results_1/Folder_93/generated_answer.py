from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):
    min_length = 3
    combs = []
    count_anagrams = 0
    for word in set(words):
        if len(word) >= min_length:
            for comb in combinations(sorted(words), 2):
                if Counter(comb[0].lower()) == Counter(comb[1].lower()) and len(comb[0]) >= min_length and (len(comb[1]) >= min_length):
                    count_anagrams += 1
                    if count_anagrams >= 18:
                        return True
    return False