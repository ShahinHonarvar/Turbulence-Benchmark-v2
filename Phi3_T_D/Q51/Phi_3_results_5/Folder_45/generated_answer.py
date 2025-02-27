from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count = sum((sorted_strings.count(s) * (sorted_strings.count(s) - 1) // 2 for s in set(sorted_strings)))
    return count <= 464