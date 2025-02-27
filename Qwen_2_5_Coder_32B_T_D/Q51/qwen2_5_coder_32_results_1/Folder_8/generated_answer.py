from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    seen = {}
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        c = Counter(sorted(s))
        key = tuple(c.items())
        if key in seen:
            anagram_count += seen[key]
        seen[key] = seen.get(key, 0) + 1
    return anagram_count <= 68