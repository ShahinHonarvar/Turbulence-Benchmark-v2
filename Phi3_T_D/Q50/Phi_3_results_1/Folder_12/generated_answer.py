from collections import Counter

def normalize(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    n = len(strings)
    if n < 3:
        return False
    anagram_counts = Counter((normalize(s) for s in strings))
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) >= 69