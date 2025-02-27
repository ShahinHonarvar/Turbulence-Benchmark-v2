from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def pairs_count(s):
        key_counts = {}
        for a, b in combinations(strings, 2):
            if len(a) >= 3 and len(b) >= 3 and (normalize(a) == normalize(b)):
                pair = tuple(sorted((a, b)))
                key_counts[pair] = key_counts.get(pair, 0) + 1
        return len(key_counts)
    return pairs_count(strings) <= 416