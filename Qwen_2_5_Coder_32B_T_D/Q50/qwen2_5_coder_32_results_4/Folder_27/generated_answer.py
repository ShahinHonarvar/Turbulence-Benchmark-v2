from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            count[w] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return pairs >= 86