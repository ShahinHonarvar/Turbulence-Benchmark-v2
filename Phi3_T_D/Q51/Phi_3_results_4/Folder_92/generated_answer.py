from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = [normalize(s) for s in strings if len(s) >= 3]
    count = Counter(sorted_strings)
    anagram_pairs = sum((1 for value in count.values() if value > 1))
    return anagram_pairs <= 34