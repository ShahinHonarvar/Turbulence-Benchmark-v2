from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagrams = [tuple(sorted(s)) for s in strings]
    count = Counter(anagrams)
    return sum((v * (v - 1) // 2 for v in count.values())) >= 9