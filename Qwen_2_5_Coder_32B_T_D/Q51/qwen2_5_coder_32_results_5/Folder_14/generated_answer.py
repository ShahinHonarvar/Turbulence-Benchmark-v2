from collections import defaultdict

def if_contains_anagrams(words):
    a = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            a[''.join(sorted(w))].append(w)
    c = sum((len(v) * (len(v) - 1) // 2 for v in a.values() if len(v) > 1))
    return c <= 474