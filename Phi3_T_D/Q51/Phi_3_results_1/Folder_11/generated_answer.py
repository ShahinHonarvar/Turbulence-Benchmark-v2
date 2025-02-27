from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings]
    unique_sorted_strings = set(sorted_strings)
    anagrams_count = sum((sorted_strings.count(s) for s in unique_sorted_strings if len(s) >= 3))
    return anagrams_count <= 41