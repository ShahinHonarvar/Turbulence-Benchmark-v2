from collections import defaultdict

def if_contains_anagrams(strings):
    sort_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = sum((sort_strings.count(key) * (sort_strings.count(key) - 1) // 2 for key in set(sort_strings)))
    return anagram_count >= 47