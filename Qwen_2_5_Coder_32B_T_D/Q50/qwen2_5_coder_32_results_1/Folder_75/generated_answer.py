from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    count = 0
    words = [word.lower() for word in words if len(word) >= 3]
    for a, b in combinations(words, 2):
        if Counter(a) == Counter(b):
            count += 1
    return count >= 70