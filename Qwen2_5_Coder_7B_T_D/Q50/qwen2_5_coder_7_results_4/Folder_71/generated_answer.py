from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for s in lst:
        if len(s) >= 3:
            count = Counter(s.lower())
            if sum(count.values()) >= 3:
                anagram_pairs += 1
    return anagram_pairs >= 57