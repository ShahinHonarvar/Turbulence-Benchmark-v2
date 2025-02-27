from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3 and s.isalpha()]
    normalized_strings = [normalize(s) for s in filtered_strings]
    counter = Counter(normalized_strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return anagram_pairs <= 173