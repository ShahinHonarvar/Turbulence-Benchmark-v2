def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_set = set((normalize(s) for s in lst if len(s) >= 3))
    count = sum((1 for a in normalized_set for b in normalized_set if a < b and len(a) == len(b) and (sorted(a) == sorted(b))))
    return count <= 25