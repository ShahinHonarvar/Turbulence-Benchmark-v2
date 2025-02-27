from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            c = Counter(sorted(s))
            key = tuple(c.items())
            if key in anagrams:
                count += anagrams[key]
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return count <= 423