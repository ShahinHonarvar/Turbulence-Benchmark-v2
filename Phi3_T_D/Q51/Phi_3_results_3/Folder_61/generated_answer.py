from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = Counter(sorted_strings)
    return sum((1 for count in anagram_count.values() if count >= 2)) <= 50