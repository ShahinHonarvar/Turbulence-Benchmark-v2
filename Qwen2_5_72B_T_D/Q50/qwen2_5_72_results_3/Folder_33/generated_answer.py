from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    counts = Counter(sorted_strings)
    anagrams_count = sum([1 for count in counts.values() if count > 1])
    return anagrams_count >= 140