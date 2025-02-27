from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    processed = [Counter(s.lower()) for s in lst if len(s) >= 3]
    for combo in combinations(processed, 2):
        if combo[0] == combo[1]:
            anagram_pairs += 1
    return anagram_pairs >= 96