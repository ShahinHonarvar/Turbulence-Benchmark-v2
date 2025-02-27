from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    anagram_counts = Counter(sorted_strings)
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs >= 78