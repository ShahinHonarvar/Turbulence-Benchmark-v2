from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_count[w] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs >= 188