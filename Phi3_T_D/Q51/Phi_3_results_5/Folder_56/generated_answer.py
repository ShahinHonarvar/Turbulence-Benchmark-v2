from collections import Counter, defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = Counter((normalize(s) for s in strings if 2 < len(s) < 24))
    return sum((val > 1 for val in count.values())) <= 11