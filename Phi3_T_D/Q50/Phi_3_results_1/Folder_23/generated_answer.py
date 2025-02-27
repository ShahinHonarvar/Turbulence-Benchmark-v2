from itertools import combinations

def if_contains_anagrams(words):
    anagram_count = 0
    for a, b in combinations(words, 2):
        if sorted(a.lower()) == sorted(b.lower()) and len(a) >= 3:
            anagram_count += 1
            if anagram_count >= 67:
                return True
    return False