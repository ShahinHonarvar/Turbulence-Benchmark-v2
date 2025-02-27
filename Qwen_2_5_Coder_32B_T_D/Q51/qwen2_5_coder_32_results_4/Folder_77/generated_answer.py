from collections import defaultdict

def if_contains_anagrams(words):
    a = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            a[w] += 1
    pairs = sum((v * (v - 1) // 2 for v in a.values()))
    return pairs <= 17