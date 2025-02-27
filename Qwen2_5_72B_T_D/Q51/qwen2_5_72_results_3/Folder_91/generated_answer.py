from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_pairs = Counter((tuple(sorted(s)) for s in strings))
    count = sum((1 for count in anagram_pairs.values() if count > 1))
    return count <= 88