from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    for group in anagrams.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 43