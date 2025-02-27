from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(w1, w2):
        return Counter(w1) == Counter(w2)
    words = [w.lower() for w in words if len(w) >= 3]
    anagram_count = 0
    for w1, w2 in combinations(words, 2):
        if is_anagram(w1, w2):
            anagram_count += 1
            if anagram_count > 77:
                return False
    return True