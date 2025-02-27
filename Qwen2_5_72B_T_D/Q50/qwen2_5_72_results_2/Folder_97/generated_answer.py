from collections import Counter

def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    counts = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs >= 123