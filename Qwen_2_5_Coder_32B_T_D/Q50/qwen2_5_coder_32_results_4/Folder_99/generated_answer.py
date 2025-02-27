from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return pairs >= 314