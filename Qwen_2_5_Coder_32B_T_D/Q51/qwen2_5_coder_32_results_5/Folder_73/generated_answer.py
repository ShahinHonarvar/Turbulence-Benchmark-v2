from collections import defaultdict

def if_contains_anagrams(words):
    d = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            d[w] += 1
    count = 0
    for v in d.values():
        count += v * (v - 1) // 2
    return count <= 279