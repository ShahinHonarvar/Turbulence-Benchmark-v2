from collections import Counter

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    normalized_strings = [normalize(s) for s in valid_strings]
    anagram_counts = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 464