from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    count = Counter(sorted_strings)
    anagram_pairs = sum((n * (n - 1) // 2 for n in count.values()))
    return anagram_pairs >= 177