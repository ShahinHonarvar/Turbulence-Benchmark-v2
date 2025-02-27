from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    string_counts = Counter((normalize(s) for s in strings if len(s) >= 3))
    return sum((1 for count in string_counts.values() if count > 1)) <= 35