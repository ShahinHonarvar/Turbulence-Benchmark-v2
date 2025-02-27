from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    seen = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            c = Counter(sorted(s))
            if c in seen:
                anagram_count += seen[c]
                seen[c] += 1
            else:
                seen[c] = 1
    return anagram_count <= 67