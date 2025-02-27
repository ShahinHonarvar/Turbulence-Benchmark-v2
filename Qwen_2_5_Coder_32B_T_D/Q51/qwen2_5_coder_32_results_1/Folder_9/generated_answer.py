from collections import defaultdict

def if_contains_anagrams(words):
    counter = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            counter[''.join(sorted(word))] += 1
    pair_count = sum((v * (v - 1) // 2 for v in counter.values()))
    return pair_count <= 475