from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    strings = [s for s in strings if len(s) >= 3]
    normalized_counts = Counter((normalize(s) for s in strings))
    anagram_pairs = sum((count * (count - 1) // 2 for count in normalized_counts.values()))
    return anagram_pairs >= 10