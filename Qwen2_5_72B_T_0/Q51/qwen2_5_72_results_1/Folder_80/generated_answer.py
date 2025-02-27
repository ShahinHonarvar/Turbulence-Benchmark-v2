from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_pairs = 0
    seen = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in seen:
            anagram_pairs += seen[sorted_s]
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
    return anagram_pairs <= 255