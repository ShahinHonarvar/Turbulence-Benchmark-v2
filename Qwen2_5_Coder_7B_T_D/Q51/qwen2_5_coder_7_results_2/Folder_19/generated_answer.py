from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return Counter(w1.lower()) == Counter(w2.lower())
    count = 0
    for w1, w2 in combinations(words, 2):
        if len(w1) >= 3 and len(w2) >= 3 and is_anagram(w1, w2):
            count += 1
    return count <= 69