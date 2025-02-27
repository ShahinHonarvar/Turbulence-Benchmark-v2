from collections import defaultdict

def if_contains_anagrams(strings):
    s = defaultdict(int)
    for string in strings:
        w = ''.join(sorted(string.lower()))
        if len(w) > 2:
            s[w] += 1
    pairs = sum((v * (v - 1) // 2 for v in s.values()))
    return pairs <= 277