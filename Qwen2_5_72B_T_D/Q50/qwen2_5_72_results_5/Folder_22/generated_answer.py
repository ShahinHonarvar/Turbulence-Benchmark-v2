from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagram_counter = Counter([''.join(sorted(s)) for s in strings if len(s) >= 3])
    pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return pairs >= 72