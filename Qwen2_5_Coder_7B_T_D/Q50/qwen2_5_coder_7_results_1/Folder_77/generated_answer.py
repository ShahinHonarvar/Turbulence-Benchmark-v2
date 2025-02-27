from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            counter = Counter(s)
            for c in counter:
                if counter[c] > 1:
                    anagram_pairs += counter[c] - 1
    return anagram_pairs >= 209