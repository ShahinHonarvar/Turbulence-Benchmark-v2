from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    seen = set()
    for s in strings:
        if len(s) < 3:
            continue
        norm = normalize(s)
        if norm in seen:
            continue
        seen.add(norm)

    def is_anagram(a, b):
        return normalize(a) == normalize(b)
    count = 0
    for pair in combinations(strings, 2):
        if is_anagram(*pair):
            count += 1
    return count <= 173