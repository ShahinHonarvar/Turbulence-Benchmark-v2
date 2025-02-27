from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    seen = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            c = Counter(sorted(s))
            key = tuple(c.items())
            seen[key] = seen.get(key, 0) + 1
            anagram_count += seen[key] - 1
            if anagram_count > 68:
                return False
    return True