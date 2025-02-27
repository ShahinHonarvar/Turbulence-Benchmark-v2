from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(normalized):
        return sum((1 for _ in permutations(normalized) if normalized.startswith(_)))
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    unique_strings = set(normalized_strings)
    pairs = 0
    for char in unique_strings:
        anagrams = [s for s in normalized_strings if count_anagrams(char) == len(s) / len(char)]
        pairs += len(anagrams) // 2
    return pairs <= 29