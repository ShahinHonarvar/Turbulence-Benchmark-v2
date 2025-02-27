import collections

def if_contains_anagrams(strings):
    anagram_pairs = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    strings_sorted = [''.join(sorted(s)) for s in strings]
    counter = collections.Counter(strings_sorted)
    anagram_pairs = sum((val * (val - 1) // 2 for val in counter.values() if val >= 2))
    return anagram_pairs <= 22