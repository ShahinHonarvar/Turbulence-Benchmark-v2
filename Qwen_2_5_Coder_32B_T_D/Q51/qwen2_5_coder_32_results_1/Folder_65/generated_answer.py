from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            count[word] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs <= 72