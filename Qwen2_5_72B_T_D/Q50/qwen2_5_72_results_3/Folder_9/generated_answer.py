from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3]
    normalized_strings = [normalize(s) for s in filtered_strings]
    anagram_counts = Counter(normalized_strings)
    pairs = 0
    for count in anagram_counts.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 66