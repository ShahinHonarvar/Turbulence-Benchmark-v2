from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    strings = [s for s in strings if len(s) >= 3]
    normalized_strings = [normalize(s) for s in strings]
    counts = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs >= 46