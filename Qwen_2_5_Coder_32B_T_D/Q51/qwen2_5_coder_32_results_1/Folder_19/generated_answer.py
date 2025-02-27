from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(words):
    d = defaultdict(list)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            d[w].append(word)
    pairs = sum((len(list(combinations(v, 2))) for v in d.values()))
    return pairs <= 69