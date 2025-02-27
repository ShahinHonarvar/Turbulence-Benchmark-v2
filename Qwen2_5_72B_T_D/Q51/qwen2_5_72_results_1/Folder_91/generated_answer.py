from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    filtered_strings = [s for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_counts = Counter((normalize(s) for s in filtered_strings))
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 88