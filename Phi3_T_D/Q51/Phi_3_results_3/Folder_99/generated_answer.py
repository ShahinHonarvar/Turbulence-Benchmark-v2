from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def valid_length(s):
        return len(s) >= 3
    normalized_strings = [normalize(s) for s in strings if valid_length(s)]
    anagram_counts = defaultdict(int)
    for s in normalized_strings:
        anagram_counts[s] += 1
    return sum((x > 1 for x in anagram_counts.values())) <= 93