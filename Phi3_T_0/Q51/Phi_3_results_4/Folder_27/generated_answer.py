from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(normalized_strings):
        counts = Counter(normalized_strings)
        return sum((count * (count - 1) // 2 for count in counts.values()))
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    return count_anagrams(normalized_strings) <= 113