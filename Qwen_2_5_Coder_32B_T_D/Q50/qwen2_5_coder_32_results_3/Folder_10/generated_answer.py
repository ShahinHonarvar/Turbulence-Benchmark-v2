from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            count[''.join(sorted(word))] += 1
    pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return pairs >= 52