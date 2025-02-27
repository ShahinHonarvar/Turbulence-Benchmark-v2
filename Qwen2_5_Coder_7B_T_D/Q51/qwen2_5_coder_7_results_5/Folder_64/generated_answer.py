from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word = sorted(word.lower())
            d[tuple(word)].append(word)
    count = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return count <= 59