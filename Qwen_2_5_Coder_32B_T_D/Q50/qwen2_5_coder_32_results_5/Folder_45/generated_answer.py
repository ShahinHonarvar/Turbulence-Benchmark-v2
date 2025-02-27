from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for w in words:
        w = w.lower()
        if len(w) >= 3:
            sorted_w = ''.join(sorted(w))
            count[sorted_w] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return pairs >= 277