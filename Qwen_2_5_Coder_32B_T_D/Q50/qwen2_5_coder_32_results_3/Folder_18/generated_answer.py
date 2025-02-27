from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        wsorted = ''.join(sorted(word.lower()))
        if len(wsorted) >= 3:
            count[wsorted] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs >= 106