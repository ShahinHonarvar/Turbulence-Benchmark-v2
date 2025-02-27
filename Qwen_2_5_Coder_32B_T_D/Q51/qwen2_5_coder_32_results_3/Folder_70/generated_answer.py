from collections import defaultdict

def if_contains_anagrams(words):
    cnt = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            cnt[w] += 1
    pairs = sum((v * (v - 1) // 2 for v in cnt.values()))
    return pairs <= 97