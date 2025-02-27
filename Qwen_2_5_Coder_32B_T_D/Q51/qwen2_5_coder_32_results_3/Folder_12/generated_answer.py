from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    seen = {}
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            count = seen.get(s, 0)
            anagram_count += count
            seen[s] = count + 1
    return anagram_count <= 92