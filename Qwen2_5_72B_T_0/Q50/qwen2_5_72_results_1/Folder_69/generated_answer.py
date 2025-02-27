from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    anagram_counts = Counter(sorted_strings)
    pairs = 0
    for count in anagram_counts.values():
        pairs += count * (count - 1) // 2
    return pairs >= 188