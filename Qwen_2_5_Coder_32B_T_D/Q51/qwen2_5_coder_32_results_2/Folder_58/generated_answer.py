from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    seen = {}
    for word in lst:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            if w in seen:
                seen[w].append(word)
            else:
                seen[w] = [word]
    for anagrams in seen.values():
        count += len(list(combinations(anagrams, 2)))
    return count <= 60